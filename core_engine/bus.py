from typing import Dict, List  # For type annotations
import logging  # For logging messages and errors

# Creating a logger for the Agent System
logger = logging.getLogger("AgentSystem")

# MessageBus handles communication between agents
class MessageBus:
    def __init__(self):
        # Dictionary to hold agents by their unique IDs
        self.agents: Dict[str, object] = {}

        # Dictionary to hold channel subscriptions (each channel maps to a list of agent objects)
        self.subscriptions: Dict[str, List[object]] = {}

        # List to keep a log of all messages sent through the bus
        self.message_log = []

    def register(self, agent):
        """Register agent for direct messaging"""
        self.agents[agent.config.id] = agent  # Store the agent using its config ID as the key
        logger.info(f"Registered agent {agent.config.id}")  # Log registration

    def subscribe(self, channel: str, agent):
        """Subscribe agent to a channel"""
        if channel not in self.subscriptions:
            self.subscriptions[channel] = []  # Initialize the channel if not present
        self.subscriptions[channel].append(agent)  # Add the agent to the channel
        logger.info(f"Agent {agent.config.id} subscribed to {channel}")  # Log the subscription

    async def send(self, agent_id: str, message):
        """Send direct message to agent"""
        if agent_id in self.agents:
            self.message_log.append(message)  # Log the message
            await self.agents[agent_id].handle(message)  # Deliver the message to the agent's handle method
        else:
            logger.error(f"Agent {agent_id} not found")  # Log an error if agent is not registered

    async def publish(self, channel: str, message):
        """Publish message to all subscribers of a channel"""
        if channel in self.subscriptions:
            for agent in self.subscriptions[channel]:  # Iterate over all subscribed agents
                await self.send(agent.config.id, message)  # Send the message to each subscriber
