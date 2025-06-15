# tests/test_task_manager_agent.py
import unittest
from prodigal_agent.agents.task_manager_agent import TaskManagerAgent
from prodigal_agent.schemas.agent_config import AgentConfig

class TestTaskManagerAgent(unittest.TestCase):
    def test_task_manager_can_be_instantiated(self):
        config = AgentConfig(name="TaskManagerAgent", role="manager", goal="testing")
        agent = TaskManagerAgent(config=config)
        self.assertEqual(agent.name, "TaskManagerAgent")
        self.assertEqual(agent.config.role, "manager")

if __name__ == "__main__":
    unittest.main()
