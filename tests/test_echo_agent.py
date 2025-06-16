def test_echo_agent_response(mocker):
    from MultiProdigy.agents.echo_agent import EchoAgent
    from MultiProdigy.schemas.message import Message
    from MultiProdigy.bus.bus import MessageBus

    bus = MessageBus()
    agent = EchoAgent(name="echo", bus=bus)
    mock_publish = mocker.patch.object(bus, 'publish')

    msg = Message(sender="user", receiver="echo", content="Hello")
    agent.bus.register(agent)
    agent.on_message(msg)

    assert mock_publish.called
    reply = mock_publish.call_args[0][0]
    assert reply.content == "Echo: Hello"
    assert reply.receiver == "user"