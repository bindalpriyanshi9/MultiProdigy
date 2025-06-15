<<<<<<< HEAD
from prodigal_agent.agents.agent_base import BaseAgent
from prodigal_agent.schemas.message import Message

class UserAgent(BaseAgent):
    def receive_message(self, message):
        if isinstance(message, dict):
            message = Message(**message)
        print(f"[{self.name}] Received: {message.content}")
=======
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
>>>>>>> upstream/main
