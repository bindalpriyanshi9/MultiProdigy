from fastapi import FastAPI  # Importing FastAPI to create the web API
from .runtime import AgentRuntime  # Importing the runtime manager that handles agent execution
from .config_model import AgentConfig  # Importing the config model for initializing agents
from .echo_agent import EchoAgent  # Importing a specific agent implementation (EchoAgent)

# Creating a FastAPI application instance
app = FastAPI()

# Initializing the agent runtime system (manages agent lifecycle and messaging)
runtime = AgentRuntime()

# Event handler to run on application startup
@app.on_event("startup")
async def startup():
    # Creating an EchoAgent with ID 'echo1' using configuration
    echo = EchoAgent(AgentConfig(id="echo1"))
    
    # Registering the echo agent into the messaging bus
    runtime.bus.register(echo)
    
    # Starting the runtime which may start all registered agents
    await runtime.start()

# GET endpoint to list all registered agent IDs
@app.get("/agents")
async def list_agents():
    return list(runtime.bus.agents.keys())  # Returns a list of registered agent IDs

# POST endpoint to send a message to a specific agent by its ID
@app.post("/send/{agent_id}")
async def send_message(agent_id: str, message: dict):
    # Sends the message to the specified agent using the message bus
    await runtime.bus.send(agent_id, message)
    
    # Responds with a confirmation
    return {"status": "sent"}
