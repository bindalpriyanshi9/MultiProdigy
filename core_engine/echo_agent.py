from .agent_base import Agent  # Abstract base class for all agents
from .config_model import Message  # Pydantic model for message validation
from typing import Dict, Any  # For type hinting
import logging  # Logging module for debug/info/error tracking

logger = logging.getLogger("AgentSystem")  # Logger instance for this module

# A simple agent that echoes back received messages
class EchoAgent(Agent):
    def __init__(self, config):
        self.config = config  # Agent configuration (includes ID, etc.)
        self._running = False  # Internal flag to control the running state
        self.echo_count = 0  # Counter to track number of messages handled

    # Starts the agent by setting the running flag to True
    async def start(self):
        self._running = True
        logger.info(f"{self.config.id} started")  # Log startup

    # Stops the agent and logs the number of messages processed
    async def stop(self):
        self._running = False
        logger.info(f"{self.config.id} stopped after {self.echo_count} messages")

    # Handles incoming messages by echoing them back to the sender
    async def handle(self, message: Dict[str, Any]):
        validated = Message.parse_obj(message)  # Validate and parse the incoming message
        self.echo_count += 1  # Increment message counter
        logger.info(f"Echo processed message #{self.echo_count}")  # Log message count
        return {
            "sender": self.config.id,  # Echo agent's ID
            "receiver": validated.sender,  # Send back to original sender
            "content": {"echo": validated.content}  # Echo the original content
        }

    # Optional processing loop (not used in this simple agent)
    async def process(self):
        while self._running:
            await asyncio.sleep(1)  # Sleep to simulate continuous background processing
