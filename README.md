<<<<<<< HEAD
# Agent Framework

A Python framework for building concurrent, message-driven agent systems with strong typing and configurable scheduling.

## Features

- **Type-safe agents**: Pydantic-validated configuration and messages
- **Flexible messaging**: Both pub/sub and direct RPC patterns
- **Priority scheduling**: Configurable execution priorities
- **Lifecycle management**: Clean startup/shutdown procedures
- **Thread-safe**: Built on asyncio for concurrency safety

## Installation

```bash
pip install agent-framework

For development:
git clone https://github.com/Ayushi-000/agent-framework.git
cd agent-framework
pip install -e .[dev]

Quick Start
Create an agent:
from agent_framework import Agent, AgentConfig

class MyAgent(Agent):
    async def handle_message(self, msg):
        print(f"Received: {msg}")
Configure and run:
from agent_framework import MessageBus, PriorityScheduler

config = AgentConfig(id="agent1")
agent = MyAgent(config)
bus = MessageBus()
scheduler = PriorityScheduler()

scheduler.add_agent(agent)
await scheduler.run()

# Send a message
await bus.send("agent1", {"text": "Hello"})

Documentation
Core Components
File	Purpose
core/agent.py	Base Agent abstract class
core/bus.py	Message routing (pub/sub + direct)
core/scheduler.py	Execution control
models/config.py	Pydantic model definitions

Agent Interface:
class MyAgent(Agent):
    async def start(self):
        """Initialize resources"""
    
    async def handle_message(self, msg: dict):
        """Process incoming messages"""
    
    async def terminate(self):
        """Cleanup resources"""
Message Bus API:
bus = MessageBus()

# Pub/sub
bus.subscribe("channel", agent)
await bus.publish("channel", {"data": 123})

# Direct
await bus.send("agent_id", {"command": "stop"})
Examples
Priority Scheduling
high_priority = AgentConfig(id="critical", priority=1)
low_priority = AgentConfig(id="background", priority=5)

scheduler.add_agents([
    CriticalAgent(high_priority),
    BackgroundAgent(low_priority)
])
Validated Messages
from pydantic import BaseModel

class SensorMessage(BaseModel):
    sensor_id: str
    value: float
    timestamp: datetime

msg = SensorMessage(sensor_id="temp1", value=22.5)
await bus.send("logger", msg.dict())

Development
Running Tests
pytest tests/ --cov=agent_framework --cov-report=html
Building Docs
pip install pdoc
pdoc --html agent_framework -o docs
Contributing
We welcome contributions! Please:

Fork the repository

Create a feature branch

Submit a pull request with:

Tests for new features

Updated documentation

Type hints for public methods

License
MIT License - See LICENSE for details.

This version:

1. Has perfect GitHub Markdown formatting
2. Includes all essential sections in a logical flow
3. Provides clear, copy-pasteable code examples
4. Maintains professional tone while being approachable
5. Links to license file (create a LICENSE file)
6. Uses consistent heading levels
7. Includes both user and developer documentation
8. Has clear contribution guidelines
9. Is properly spaced for readability on GitHub


























=======
## Documentation

- [Getting Started](docs/getting_started.md)  
- [Architecture](docs/architecture.md)  
- [Module Reference](docs/modules_reference.md)  
- [Sample Demo](docs/sample_agent_demo.md)  
>>>>>>> upstream/main
