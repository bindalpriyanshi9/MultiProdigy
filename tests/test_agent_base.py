def test_base_agent_send(mocker):
    from MultiProdigy.agents.agent_base import BaseAgent
    from MultiProdigy.bus.bus import MessageBus
    from MultiProdigy.schemas.message import Message

    class DummyAgent(BaseAgent):
        def on_message(self, message):
            pass

    bus = MessageBus()
    agent = DummyAgent(name="test", bus=bus)
    mock_publish = mocker.patch.object(bus, 'publish')

    agent.send("Hello", "receiver")

    assert mock_publish.called
    msg = mock_publish.call_args[0][0]
    assert isinstance(msg, Message)
    assert msg.sender == "test"
    assert msg.receiver == "receiver"
    assert msg.content == "Hello"