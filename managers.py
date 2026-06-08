# managers.py
class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, websocket, client_id):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id):
        if client_id in self.active_connections:
            del self.active_connections[client_id]

    async def send_personal_message(self, message, client_id):
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_text(message)

class MatchManager:
    def __init__(self):
        self.waiting_queue = []
        self.matches = {}

    def add_to_queue(self, user_id):
        if user_id in self.matches: return None, None
        if user_id not in self.waiting_queue:
            self.waiting_queue.append(user_id)
        if len(self.waiting_queue) >= 2:
            u1, u2 = self.waiting_queue.pop(0), self.waiting_queue.pop(0)
            self.matches[u1] = u2
            self.matches[u2] = u1
            return u1, u2
        return None, None

# Singleton အနေနဲ့ တစ်ခုပဲ ဆောက်ပေးထားမယ်
manager = ConnectionManager()
match_manager = MatchManager()