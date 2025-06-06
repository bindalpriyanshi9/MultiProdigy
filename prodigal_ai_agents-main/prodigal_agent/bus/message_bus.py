# prodigal_agent/bus/message_bus.py

class MessageBus:
    def __init__(self):
        self.agents = []

    def register_agent(self, agent):
        self.agents.append(agent)
        print(f"Agent registered: {agent}")
