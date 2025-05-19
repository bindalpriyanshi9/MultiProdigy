# core_engine/demo.py

import asyncio  # For asynchronous execution
from runtime import AgentRuntime  # Manages the agent lifecycle and message routing
from user_agent import UserAgent  # A custom user agent class
from echo_agent import EchoAgent  # A simple echo agent class
from config_model import AgentConfig  # Configuration model for agents

# Main asynchronous function to run the agent system
async def main():
    runtime = AgentRuntime()  # Initialize the runtime system

    # Create agent instances with unique IDs and priorities
    user = UserAgent(AgentConfig(id="user1", priority=1))
    echo = EchoAgent(AgentConfig(id="echo1", priority=2))

    # Register agents with the message bus
    runtime.bus.register(user)
    runtime.bus.register(echo)

    # Subscribe echo agent to the "broadcast" channel (for pub/sub messaging)
    runtime.bus.subscribe("broadcast", echo)

    # Start the entire runtime system and individual agents
    await runtime.start()
    await user.start()
    await echo.start()

    # Send a direct message to echo agent from user agent
    await runtime.bus.send("echo1", {"sender": "user1", "content": "Direct message"})

    # Publish a message to all subscribers of the "broadcast" channel
    await runtime.bus.publish("broadcast", {"sender": "user1", "content": "Pub/sub message"})

    # Let the system run for 5 seconds
    await asyncio.sleep(5)

    # Gracefully stop agents and runtime
    await echo.stop()
    await user.stop()
    await runtime.stop()

# Entry point to start the async main function when the script is run directly
if __name__ == "__main__":
    asyncio.run(main())
