# main.py
from prodigal_agent.agents.task_manager_agent import TaskManagerAgent
from prodigal_agent.schemas.agent_config import AgentConfig

if __name__ == "__main__":
    config = AgentConfig(name="TaskManagerAgent", role="manager", goal="Manage all tasks")
    agent = TaskManagerAgent(config=config)
    agent.run()
