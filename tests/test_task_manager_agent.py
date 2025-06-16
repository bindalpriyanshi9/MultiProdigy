def test_task_manager_agent_instantiation():
    from MultiProdigy.agents.task_manager_agent import TaskManagerAgent
    from MultiProdigy.schemas.agent_config import AgentConfig
    from MultiProdigy.bus.bus import MessageBus

    config = AgentConfig(name="Manager", role="task", goal="testing")
    bus = MessageBus()

    class DummyTM(TaskManagerAgent):
        def __init__(self):
            super().__init__(config=config, bus=bus)

        def on_message(self, message):
            pass

    agent = DummyTM()
    assert agent.name == "Manager"
