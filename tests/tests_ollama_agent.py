import unittest
from MultiProdigy.agents.ollama_agent import OllamaAgent
from MultiProdigy.bus.message_bus import MessageBus
from MultiProdigy.schemas.message import Message


class TestOllamaAgent(unittest.TestCase):
    def test_ollama_response_format(self):
        bus = MessageBus()
        ollama_agent = OllamaAgent(name="ollama_agent", bus=bus)

        response_holder = {}

        def capture_response(msg):
            response_holder["response"] = msg.content

        bus.register_agent("task_agent", capture_response)

        test_message = Message(
            sender="task_agent",
            receiver="ollama_agent",
            content="Hello! What's your name?"
        )
        bus.dispatch_message(test_message)

        self.assertIn("Ollama", response_holder["response"] or "No Response")


if __name__ == '__main__':
    unittest.main()
