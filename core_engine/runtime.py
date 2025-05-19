from .bus import MessageBus  # Import MessageBus for message routing between agents
from .scheduler import PriorityScheduler  # Import scheduler to manage agent task priorities
import logging  # Standard Python logging module

logger = logging.getLogger("AgentSystem")  # Logger instance for this module

# Core runtime class managing agents, messaging, and scheduling
class AgentRuntime:
    def __init__(self):
        self.bus = MessageBus()  # Initialize the message bus for inter-agent communication
        self.scheduler = PriorityScheduler()  # Initialize scheduler for agent execution ordering
        self._active_agents = set()  # Track active agent IDs currently running

    # Spawn a new agent: register it, add to active set, and start it asynchronously
    async def spawn(self, agent):
        self.bus.register(agent)  # Register the agent with the message bus
        self._active_agents.add(agent.config.id)  # Add agent ID to active set
        await agent.start()  # Start the agent's async execution
        logger.info(f"Spawned agent {agent.config.id}")  # Log spawn event

    # Terminate a running agent by its ID: call terminate and remove from active set
    async def terminate(self, agent_id):
        if agent_id in self.bus.agents:
            await self.bus.agents[agent_id].terminate()  # Call agent's termination method
            self._active_agents.remove(agent_id)  # Remove from active set
            logger.info(f"Terminated agent {agent_id}")  # Log termination event
