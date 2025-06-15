from MultiProdigy.agents.agent_base import BaseAgent
from MultiProdigy.schemas.message import Message

class HelloAgent(BaseAgent):
    def __init__(self, name: str, bus):
        super().__init__(name=name, bus=bus)
        self.bus.register(self)

    def on_message(self, message: Message) -> None:
        response = message.copy_with_new_content(
            f"Hello from {self.name}! You said: {message.content}"
        )
        response.sender = self.name
        response.receiver = message.sender
        self.bus.publish(response)