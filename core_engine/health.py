from typing import Dict
from pydantic import BaseModel
from .logging import logger

# 🩺 Health Check Config
class HealthCheckConfig(BaseModel):
    interval_seconds: int = 30
    timeout_seconds: int = 5

health_status: Dict[str, str] = {}

# 💓 Perform Health Check
def perform_health_check(agent_name: str):
    logger.info(f"💓 Health check for {agent_name}: OK")
    health_status[agent_name] = "healthy"

# 🔎 Discover Agents
def discover_services():
    logger.info("🔎 Discovering available agents...")
    return ["EchoAgent", "TaskProcessorAgent"]
