from schemas.agent_config import LLMSettings
import os
import yaml

def load_llm_settings() -> LLMSettings:
    if os.path.exists("config.yaml"):
        with open("config.yaml", "r") as f:
            data = yaml.safe_load(f)
        return LLMSettings(**data)
    else:
        return LLMSettings()