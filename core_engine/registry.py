# core_engine/registry.py

class Registry:
    _schemas = {}

    @classmethod
    def register_schema(cls, name, schema):
        cls._schemas[name] = schema

    @classmethod
    def get_schema(cls, name):
        return cls._schemas.get(name)
