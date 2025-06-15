# prodigal_agent/schemas/agent_config.py
from pydantic import BaseModel

class AgentConfig(BaseModel):
    name: str
    role: str = "default"
    goal: str = "default goal"
