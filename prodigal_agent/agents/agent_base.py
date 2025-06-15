<<<<<<< HEAD
from prodigal_agent.schemas.message import Message

class BaseAgent:
    def __init__(self, name, bus):
        self.name = name
        self.bus = bus

    def send_message(self, content, recipient):
        message = Message(sender=self.name, recipient=recipient, content=content)
        self.bus.publish(message)

    def receive_message(self, message: Message):
        raise NotImplementedError("Each agent must implement the receive_message method.")
=======
# prodigal_agent/agents/agent_base.py
from prodigal_agent.schemas.agent_config import AgentConfig

class Agent:
    def __init__(self, config: AgentConfig):
        self.name = config.name
        self.config = config

    def run(self):
        print(f"{self.name} is running with goal: {self.config.goal}")
>>>>>>> upstream/main
