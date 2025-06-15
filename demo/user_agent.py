from MultiProdigy.agents.agent_base import BaseAgent
from MultiProdigy.schemas.message import Message

class UserAgent(BaseAgent):
    def __init__(self, name: str, bus):
        super().__init__(name=name, bus=bus)
        self.bus.register(self)

    def on_message(self, message: Message) -> None:
        print(f"[{self.name}] Received: {message.content}")

    def send_hello(self, to: str) -> None:
        self.send("Hello, MultiProdigy!", to)