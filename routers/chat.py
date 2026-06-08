from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status, Depends, HTTPException
from sqlalchemy.orm import Session
import token_util, schemas
from database import get_db, SessionLocal
from oauth2 import oauth2_scheme
from managers import manager, match_manager
from repository import chat_repo # Repository ကို import လုပ်ပါ

router = APIRouter(tags=["Chat"])

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int, token: str = None):
    if not token:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    try:
        token_util.verify_token(token, credentials_exception=HTTPException(status_code=401))
    except:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    await manager.connect(websocket, client_id)
    db = SessionLocal() 
    try:
        while True:
            data = await websocket.receive_text()
            target_id = match_manager.matches.get(client_id)
            
            if target_id:
                # Repository ကို ခေါ်သုံးခြင်း
                chat_repo.save_message(db, sender_id=client_id, receiver_id=target_id, content=data)
                
                await manager.send_personal_message(f"You sent: {data}", client_id)
                await manager.send_personal_message(f"New message: {data}", target_id)
            else:
                await manager.send_personal_message("System: Still waiting for a match!", client_id)
            
    except WebSocketDisconnect:
        manager.disconnect(client_id)
        partner_id = match_manager.matches.get(client_id)
        if partner_id:
            await manager.send_personal_message("System: Your partner has left.", partner_id)
            match_manager.matches.pop(client_id, None)
            match_manager.matches.pop(partner_id, None)
    finally:
        db.close()

@router.post("/match/{user_id}", dependencies=[Depends(oauth2_scheme)])
def find_match(user_id: int):
    u1, u2 = match_manager.add_to_queue(user_id)
    if u1 and u2:
        return {"status": "Matched!", "your_partner": u2 if user_id == u1 else u1}
    return {"status": "Waiting for a partner..."}

@router.get("/messages/{user_id}/{partner_id}", response_model=list[schemas.Message], dependencies=[Depends(oauth2_scheme)])
def get_chat_history(user_id: int, partner_id: int, db: Session = Depends(get_db)):
    # Repository ကို ခေါ်သုံးခြင်း
    return chat_repo.get_messages(db, user_id, partner_id)