from typing import Any, Dict  # Importing type hints for better code clarity and error checking
from core_engine.agent_base import Agent  # Importing the base Agent class (which defines abstract methods)
from core_engine.models import MessageModel  # Importing a message model (likely used elsewhere in the agent)

# EchoAgent is a concrete implementation of the abstract Agent base class
class EchoAgent(Agent):
    # This method handles incoming messages
    async def handle(self, message: Dict[str, Any]) -> Any:
        print(f"[echo] received: {message}")  # Log the received message to the console
        return f"[{self.config.id}] Echo: {message}"  # Respond with a simple echo message including the agent's ID
