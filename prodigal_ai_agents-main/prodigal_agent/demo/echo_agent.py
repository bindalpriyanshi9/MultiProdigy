
# prodigal_agent/agents/echo_agent.py

from prodigal_agent.schemas.message import Message

class EchoAgent:
    def __init__(self, name="EchoAgent"):
        self.name = name

    def handle_message(self, message: Message) -> Message:
        print(f"[{self.name}] Received message: {message.content}")
        return Message(sender=self.name, content=f"Echo: {message.content}")
