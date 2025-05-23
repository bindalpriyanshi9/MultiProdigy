from typing import Type, Dict
from pydantic import BaseModel

class SchemaRegistry:
    def __init__(self):
        self._registry: Dict[str, Type[BaseModel]] = {}

    def register_schema(self, name: str, model: Type[BaseModel]):
        self._registry[name] = model

    def get_schema(self, name: str) -> Type[BaseModel]:
        if name not in self._registry:
            raise ValueError(f"Schema '{name}' is not registered.")
        return self._registry[name]

# Create one global registry instance
registry = SchemaRegistry()
