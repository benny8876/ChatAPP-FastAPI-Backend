from sqlalchemy.orm import Session
import models

def save_message(db: Session, sender_id: int, receiver_id: int, content: str):
    new_message = models.Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

def get_messages(db: Session, user_id: int, partner_id: int):
    return db.query(models.Message).filter(
        ((models.Message.sender_id == user_id) & (models.Message.receiver_id == partner_id)) |
        ((models.Message.sender_id == partner_id) & (models.Message.receiver_id == user_id))
    ).order_by(models.Message.timestamp.asc()).all()