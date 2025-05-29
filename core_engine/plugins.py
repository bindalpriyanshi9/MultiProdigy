from pydantic import BaseModel
from .logging import logger

# 🔌 Plugin Manifest
class PluginManifest(BaseModel):
    name: str
    version: str
    entry_point: str  # e.g., "agents.echo:EchoAgent"

# 🔄 Plugin Loader
class PluginLoader:
    def __init__(self):
        self.plugins = []

    def load_plugins(self):
        # Static loading example
        example_plugin = PluginManifest(
            name="EchoAgent",
            version="0.1",
            entry_point="agents.echo:EchoAgent"
        )
        self.plugins.append(example_plugin)
        logger.info(f"🔌 Loaded plugin: {example_plugin.name} v{example_plugin.version}")
