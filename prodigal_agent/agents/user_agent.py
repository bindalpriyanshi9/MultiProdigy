# prodigal_agent/agents/user_agent.py

from prodigal_agent.schemas.schemas import Message
from prodigal_agent.agents.agent_base import BaseAgent

class UserAgent(BaseAgent):
    def __init__(self, runtime):
        super().__init__(runtime)
        self.name = "UserAgent"

    def handle_message(self, message: Message) -> str:
        print(f"[UserAgent] Received response: {message.content}")
        return message.content
