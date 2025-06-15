from prodigal_agent.agents.agent_base import BaseAgent
from prodigal_agent.bus.bus import MessageBus
from prodigal_agent.schemas.message import Message
from prodigal_agent.schemas.message import EchoResponse


class UserAgent(BaseAgent):
    def __init__(self, bus: MessageBus):
        super().__init__(name="UserAgent", bus=bus)
        self.bus.register(self)

    def handle_message(self, message: Message):
        if isinstance(message, EchoResponse):
            print(f"[UserAgent] Received: {message.content}")

    def send_message(self, content: str, receiver: str):
        print(f"[UserAgent] Sending: {content}")
        msg = Message(sender=self.name, receiver=receiver, content=content)
        self.bus.send(msg)
