from prodigal_agent.agents.agent_base import Agent
from prodigal_agent.schemas.message import Message



class HelloAgent(Agent):
    def process(self, message: Message) -> str:
        return f"Hello from {self.name}! You said: {message.content}"
