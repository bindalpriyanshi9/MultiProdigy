from pydantic import BaseModel  # Importing Pydantic's BaseModel for data validation and settings

# Configuration model for an agent
class AgentConfig(BaseModel):
    id: str  # Unique identifier for the agent (required field)

    priority: int = 1  # Optional priority field with a default value of 1

    timeout: int = 3000  # Optional timeout in milliseconds (default is 3000 ms)
