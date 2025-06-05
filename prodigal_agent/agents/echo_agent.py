# prodigal_agent/agents/echo_agent.py

from prodigal_agent.schemas.message import Message
from prodigal_agent.schemas.agent_interface import AgentInterface

class EchoAgent(AgentInterface):
    def handle_message(self, message: Message) -> Message:
        response_text = f"Echo: {message.content}"
        return Message(sender="echo_agent", content=response_text)
