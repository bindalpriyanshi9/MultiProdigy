def test_message_bus_register_and_send():
    from MultiProdigy.bus.bus import MessageBus
    from MultiProdigy.schemas.message import Message

    class DummyAgent:
        def __init__(self):
            self.name = "dummy"
            self.received = []

        def on_message(self, message):
            self.received.append(message)

    bus = MessageBus()
    agent = DummyAgent()
    bus.register(agent)
    msg = Message(sender="u", receiver="dummy", content="hello")

    bus.publish(msg)
    assert agent.received[0].content == "hello"
