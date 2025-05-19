from pydantic import BaseModel, Field  # BaseModel is used to define data validation models
import uuid  # Used to generate unique IDs
import time  # Used to get the current timestamp

# Configuration model for an agent
class AgentConfig(BaseModel):
    # Unique identifier for the agent (auto-generated using UUID if not provided)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))

    # Priority level for the agent (default is 1)
    priority: int = 1

    # Timeout duration for agent operations in seconds (default is 30.0)
    timeout: float = 30.0

# Message model to represent communication between agents
class Message(BaseModel):
    # ID of the agent sending the message
    sender: str

    # ID of the agent intended to receive the message
    receiver: str

    # Dictionary to hold the actual message content (custom data)
    content: dict

    # Timestamp of when the message was created (auto-set to current time)
    timestamp: float = Field(default_factory=time.time)

    # Unique message ID (auto-generated using UUID)
    msg_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
