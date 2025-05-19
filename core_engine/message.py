# core_engine/message.py

from pydantic import BaseModel  # Pydantic BaseModel for data validation

# Message model representing a simple message structure
class Message(BaseModel):
    sender: str      # ID or name of the message sender
    recipient: str   # ID or name of the intended message recipient
    content: str     # The actual message content as a string
