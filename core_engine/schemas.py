# core_engine/schemas.py

from pydantic import BaseModel  # Import Pydantic BaseModel for schema validation

# Schema representing configuration settings for an agent
class AgentConfig(BaseModel):
    id: str               # Unique identifier for the agent
    priority: int = 1     # Priority level for scheduling (default is 1)
    timeout: int = 1000   # Timeout duration in milliseconds (default 1000)
