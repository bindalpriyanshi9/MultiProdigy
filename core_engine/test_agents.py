import sys
from pathlib import Path
# Add parent directory to sys.path for imports from core_engine package
sys.path.insert(0, str(Path(__file__).parent.parent))

import asyncio
import logging
from core_engine.runtime import AgentRuntime  # Import the main runtime to manage agents
from core_engine.config_model import AgentConfig  # Import agent config schema
from core_engine.user_agent import UserAgent  # UserAgent implementation
from core_engine.echo_agent import EchoAgent  # EchoAgent implementation

# Configure logging to show timestamp, level, logger name, and message
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler()]
)

async def demo_all_features():
    try:
        runtime = AgentRuntime()  # Initialize the agent runtime
        
        # Create UserAgent and EchoAgent with respective configs and priorities
        user = UserAgent(AgentConfig(id="user1", priority=1))
        echo = EchoAgent(AgentConfig(id="echo1", priority=2))
        
        # Spawn (register and start) agents in the runtime
        await runtime.spawn(user)
        await runtime.spawn(echo)
        
        # Send a direct message from user1 to echo1
        await runtime.bus.send("echo1", {
            "sender": "user1",
            "receiver": "echo1", 
            "content": {"type": "direct_msg"}
        })
        
        # Subscribe echo agent to "alerts" channel (for pub/sub messaging)
        runtime.bus.subscribe("alerts", echo)
        
        # Publish a message on the "alerts" channel, echo agent will receive it
        await runtime.bus.publish("alerts", {
            "sender": "system",
            "receiver": "echo1",
            "content": {"alert": "urgent"}
        })
        
        # Allow some time for processing messages
        await asyncio.sleep(1)
        
        # Cleanly terminate agents after demo
        await runtime.terminate("user1")
        await runtime.terminate("echo1")
        
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise

# Run the async demo if this file is executed as the main program
if __name__ == "__main__":
    asyncio.run(demo_all_features())
