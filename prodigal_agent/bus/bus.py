<<<<<<< HEAD
from queue import Queue

class MessageBus:
    def __init__(self):
        self.queue = Queue()
        self.agents = {}

    def register(self, agent):
        print(f"[registry] registering agent {agent.name}")
        self.agents[agent.name] = agent

    def publish(self, message):
        print(f"[bus] publishing ▶ {message.sender} → {message.recipient}: {message.content}")
        self.queue.put(message)
        self.dispatch()

    def dispatch(self):
        while not self.queue.empty():
            message = self.queue.get()
            recipient = message.recipient
            print(f"[bus] dequeued ▶ {message.sender} → {recipient}: {message.content}")
            if recipient in self.agents:
                print(f"[bus] delivering to {recipient}")
                self.agents[recipient].receive_message(message)
            else:
                print(f"[bus] unknown recipient: {recipient}")
=======
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
>>>>>>> upstream/main
