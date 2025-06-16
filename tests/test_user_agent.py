def test_user_agent_send():
    from MultiProdigy.agents.user_agent import UserAgent
    from MultiProdigy.bus.bus import MessageBus
    from MultiProdigy.schemas.message import Message
    from MultiProdigy.agents.agent_base import BaseAgent

    class DummyEchoAgent(BaseAgent):
        def __init__(self, name, bus):
            super().__init__(name, bus)
            self.received = False

        def on_message(self, message):
            self.received = True

    bus = MessageBus()
    sender = UserAgent("UserAgent", bus)
    receiver = DummyEchoAgent("EchoAgent", bus)

    bus.register(sender)
    bus.register(receiver)

    sender.send("Hi", "EchoAgent")

    # Manual dequeue and dispatch simulation (since there's no bus.process())
    if bus.queue:
        msg = bus.queue.popleft()
        target = bus.agents.get(msg.receiver)
        if target:
            target.receive_message(msg)

    assert receiver.received
