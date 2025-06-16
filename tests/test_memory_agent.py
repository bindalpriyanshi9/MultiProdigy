def test_memory_agent_storage():
    from MultiProdigy.agents.memory_agent import MemoryAgent
    from MultiProdigy.schemas.message import Message
    from MultiProdigy.bus.bus import MessageBus

    class DummyMemoryAgent(MemoryAgent):
        def on_message(self, message):
            self.memory.append(message.content)

    bus = MessageBus()
    agent = DummyMemoryAgent("MemoryAgent", bus)
    msg = Message(sender="user", receiver="MemoryAgent", content="Remember this")

    agent.handle_message(msg)
    assert "Remember this" in agent.memory