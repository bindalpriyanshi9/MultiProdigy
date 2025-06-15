from prodigal_agent.agents.agent_base import BaseAgent
from prodigal_agent.bus.bus import MessageBus
from prodigal_agent.schemas.message import Message  # ✅ Correct location of Message
from prodigal_agent.schemas.message import Message, EchoMessage, EchoResponse


from prodigal_agent.schemas.message import Message
from prodigal_agent.bus.bus import MessageBus



class EchoAgent(BaseAgent):
    def __init__(self, bus: MessageBus):
        super().__init__(name="EchoAgent", bus=bus)
        self.bus.register(self)

    def handle_message(self, message: Message):
        print(f"[EchoAgent] Received: {message.content}")
        response = EchoResponse(
            sender=self.name,
            receiver=message.sender,
            content=f"Echo: {message.content}"
        )
        self.bus.send(response)
