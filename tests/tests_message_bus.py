import unittest
from MultiProdigy.bus.message_bus import MessageBus
from MultiProdigy.schemas.message import Message


class TestMessageBus(unittest.TestCase):
    def setUp(self):
        self.bus = MessageBus()

    def test_agent_registration(self):
        def dummy_handler(message): return None
        self.bus.register_agent("agent1", dummy_handler)
        self.assertIn("agent1", self.bus.agents)

    def test_message_dispatch(self):
        result_holder = {}

        def handler(msg):
            result_holder["content"] = msg.content

        self.bus.register_agent("agent1", handler)
        test_message = Message(sender="tester", receiver="agent1", content="Hello")
        self.bus.dispatch_message(test_message)
        self.assertEqual(result_holder["content"], "Hello")


if __name__ == '__main__':
    unittest.main()
