import asyncio
from core_engine.runtime import AgentRuntime
from core_engine.echo_agent import EchoAgent
from core_engine.config_model import AgentConfig

async def main():
    print("🚀 Starting agent system...")  # Notify start of system
    
    # Initialize the agent runtime environment
    runtime = AgentRuntime()
    
    # Create two EchoAgent instances with unique IDs and priorities
    agent1 = EchoAgent(AgentConfig(id="agent-1", priority=1))
    agent2 = EchoAgent(AgentConfig(id="agent-2", priority=2))
    
    # Register agents to the runtime - this is a synchronous operation
    runtime.register(agent1)
    runtime.register(agent2)
    
    # Send a greeting message to agent-1
    await runtime.send_message(
        "agent-1",
        {
            "sender": "system",        # Message sender ID
            "receiver": "agent-1",     # Intended recipient
            "type": "greeting",        # Message type metadata
            "content": "Hello from main system!"  # Actual message content
        }
    )
    
    # Send a status message to agent-2
    await runtime.send_message(
        "agent-2", 
        {
            "sender": "system",
            "receiver": "agent-2",
            "type": "status",
            "content": "System initialized successfully"
        }
    )
    
    # Allow agents time to process the messages asynchronously
    await asyncio.sleep(1)
    print("✅ System test completed")  # Confirm completion

if __name__ == "__main__":
    # Run the main async function in the asyncio event loop
    asyncio.run(main())
