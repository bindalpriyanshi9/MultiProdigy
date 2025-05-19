from pydantic import BaseModel  # Import BaseModel for data validation and parsing

# Model representing a message exchanged between agents
class MessageModel(BaseModel):
    sender: str    # Identifier of the message sender
    receiver: str  # Identifier of the message receiver
    content: str   # The message content as a string
