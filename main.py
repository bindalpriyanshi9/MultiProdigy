from models import TaskRequest, TaskResult
from registry import registry

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

# Runtime validation
def validate_message(message: dict):
    msg_type = message["type"]
    payload = message["payload"]

    schema_cls = registry.get_schema(msg_type)
    try:
        validated = schema_cls.parse_obj(payload)
        print("✅ Message is valid.")
        print(validated)
    except Exception as e:
        print("❌ Validation failed.")
        print(str(e))

# Call validation
validate_message(incoming_message)
