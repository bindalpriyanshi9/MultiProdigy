import logging
from pydantic import BaseModel

# 📋 Logging Configuration Model
class LoggingConfig(BaseModel):
    level: str = "INFO"
    log_file: str = "app.log"

# 🛠 Initialize Logging
logging_config = LoggingConfig()
logging.basicConfig(filename=logging_config.log_file, level=logging_config.level)
logger = logging.getLogger("AgentLogger")
