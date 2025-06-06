# prodigal_agent/agents/agent_base.py
from prodigal_agent.schemas.agent_config import AgentConfig

class Agent:
    def __init__(self, config: AgentConfig):
        self.name = config.name
        self.config = config

    def run(self):
        print(f"{self.name} is running with goal: {self.config.goal}")
