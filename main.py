import logging
from typing import Dict
from pydantic import BaseModel
from time import time
from models import TaskRequest, TaskResult
from registry import registry

# Logging Configuration

class LoggingConfig(BaseModel):
    level: str = "INFO"
    log_file: str = "app.log"

logging_config = LoggingConfig()
logging.basicConfig(filename=logging_config.log_file, level=logging_config.level)
logger = logging.getLogger("AgentLogger")

# Metrics (Simple Counter)

metrics = {
    "messages_processed": 0,
    "validation_failures": 0
}

# Error Reporting Hook

def report_error(error: Exception):
    logger.error(f"❌ Unhandled error: {str(error)}")
    # You can later expand this to send the error to an endpoint like Sentry

# Plugin Manifest & Loader

class PluginManifest(BaseModel):
    name: str
    version: str
    entry_point: str  # e.g., my_plugin:MyAgent

class PluginLoader:
    def __init__(self):
        self.plugins = []

    def load_plugins(self):
        # Dummy example - should be expanded to load from files or registry
        example_plugin = PluginManifest(
            name="EchoAgent",
            version="0.1",
            entry_point="agents.echo:EchoAgent"
        )
        self.plugins.append(example_plugin)
        logger.info(f"🔌 Loaded plugin: {example_plugin.name} v{example_plugin.version}")

plugin_loader = PluginLoader()
plugin_loader.load_plugins()

# Health Check & Discovery

class HealthCheckConfig(BaseModel):
    interval_seconds: int = 30
    timeout_seconds: int = 5

health_status: Dict[str, str] = {}

def perform_health_check(agent_name: str):
    # Dummy health check, normally you'd ping the service or test a method
    logger.info(f"💓 Health check for {agent_name}: OK")
    health_status[agent_name] = "healthy"

def discover_services():
    logger.info("🔎 Discovering available agents...")
    return ["EchoAgent", "TaskProcessorAgent"]

# Core Message Validation

# Register schemas
registry.register_schema("TaskRequest", TaskRequest)
registry.register_schema("TaskResult", TaskResult)

# Sample incoming message
incoming_message = {
    "type": "TaskRequest",
    "payload": {
        "task_id": "abc123",
        "payload": {
            "data": [1, 2, 3]
        },
        "priority": 2
    }
}

def validate_message(message: dict):
    msg_type = message["type"]
    payload = message["payload"]

    logger.info(f"📩 Validating message of type: {msg_type}")
    metrics["messages_processed"] += 1

    try:
        schema_cls = registry.get_schema(msg_type)
        validated = schema_cls.parse_obj(payload)
        print("✅ Message is valid.")
        print(validated)
        logger.info("✅ Validation successful.")
    except Exception as e:
        print("❌ Validation failed.")
        print(str(e))
        metrics["validation_failures"] += 1
        report_error(e)

# Simulate a single Agent run

validate_message(incoming_message)
perform_health_check("TaskProcessorAgent")
logger.info(f"📊 Metrics: {metrics}")
logger.info(f"🧭 Discovered services: {discover_services()}")
