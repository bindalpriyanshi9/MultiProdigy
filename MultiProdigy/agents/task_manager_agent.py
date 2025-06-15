# prodigal_agent/agents/task_manager_agent.py
from MultiProdigy.agents.agent_base import Agent
from MultiProdigy.schemas.agent_config import AgentConfig

class TaskManagerAgent(Agent):
    def __init__(self, config: AgentConfig):
        super().__init__(config=config)

    def run(self):
        print(f"{self.name} is running with role: {self.config.role}")
