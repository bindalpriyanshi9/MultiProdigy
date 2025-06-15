from prodigal_agent.agents.agent_base import BaseAgent
from prodigal_agent.schemas.message import Message

class UserAgent(BaseAgent):
    def receive_message(self, message):
        if isinstance(message, dict):
            message = Message(**message)
        print(f"[{self.name}] Received: {message.content}")
