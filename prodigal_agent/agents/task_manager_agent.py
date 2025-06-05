# prodigal_agent/agents/task_manager_agent.py
from prodigal_agent.agents.agent_base import Agent
from prodigal_agent.schemas.agent_config import AgentConfig

class TaskManagerAgent(Agent):
    def __init__(self, config: AgentConfig):
        super().__init__(config=config)

    def run(self):
        print(f"{self.name} is running with role: {self.config.role}")
