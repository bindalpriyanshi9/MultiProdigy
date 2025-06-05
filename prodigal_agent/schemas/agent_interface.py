# prodigal_agent/schema/agent_interface.py

from abc import ABC, abstractmethod
from prodigal_agent.schemas.message import Message

class AgentInterface(ABC):
    @abstractmethod
    def handle_message(self, message: Message) -> Message:
        pass
