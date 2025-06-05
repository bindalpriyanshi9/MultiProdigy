# prodigal_agent/bus/bus.py

class MessageBus:
    def __init__(self):
        self.agents = {}

    def register(self, agent):
        # Save the agent instance keyed by its name
        self.agents[agent.name] = agent

    def send(self, message):
        receiver = message.receiver
        if receiver in self.agents:
            return self.agents[receiver].handle_message(message)
        else:
            raise Exception(f"Agent {receiver} not registered in MessageBus")
