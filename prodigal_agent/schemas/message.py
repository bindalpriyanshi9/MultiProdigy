from pydantic import BaseModel

class Message(BaseModel):
    sender: str
    recipient: str  # ✅ Keep this consistent
    content: str
