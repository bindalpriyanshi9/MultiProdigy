from typing import Dict, Any
from core_engine.config_model import Message  # Import Message model for validation
import logging
import asyncio
from core_engine.agent_base import Agent  # Base abstract agent class

logger = logging.getLogger("AgentSystem")  # Logger for agent system

class UserAgent(Agent):
    def __init__(self, config):
        self.config = config
        self._running = False  # Flag to track agent running state

    async def start(self):
        """Start the agent, setting running flag and logging"""
        self._running = True
        logger.info(f"{self.config.id} started")

    async def stop(self):
        """Stop the agent and log the event"""
        self._running = False
        logger.info(f"{self.config.id} stopped")

    async def handle(self, message: Dict[str, Any]):
        """Process incoming messages by validating them using Message model"""
        try:
            validated = Message.parse_obj(message)  # Validate message structure
            logger.info(f"User received: {validated.content}")  # Log content
        except Exception as e:
            logger.error(f"Message validation failed: {str(e)}")
            raise

    async def process(self):
        """Background task loop while agent is running"""
        while self._running:
            await asyncio.sleep(1)  # Idle wait

    async def sleep(self, seconds: float):
        """Helper sleep method"""
        await asyncio.sleep(seconds)

    async def terminate(self):
        """Cleanly terminate by stopping the agent"""
        await self.stop()
