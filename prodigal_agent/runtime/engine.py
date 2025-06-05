from prodigal_agent.agents.ollama_agent import OllamaAgent
from prodigal_agent.agents.echo_agent import EchoAgent
from prodigal_agent.bus.message_bus import MessageBus 



class RuntimeEngine:
    def __init__(self):
        self.bus = MessageBus()

        self.agents = {
            "ollama_agent": OllamaAgent(),
            "echo_agent": EchoAgent()
        }

        for name, agent in self.agents.items():
            self.bus.subscribe(name, agent.handle_message)
