from prodigal_agent.agents.agent_base import BaseAgent
from prodigal_agent.schemas.message import Message

class EchoAgent(BaseAgent):
    def receive_message(self, message):
        if isinstance(message, dict):
            message = Message(**message)
        print(f"[{self.name}] Received: {message.content}")
        reply = Message(sender=self.name, recipient=message.sender, content=f"Echo: {message.content}")
        self.bus.publish(reply)
