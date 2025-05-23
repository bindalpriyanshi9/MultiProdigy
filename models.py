from pydantic import BaseModel, validator
from typing import Dict, Any, List

# Example schema: TaskRequest
class TaskRequest(BaseModel):
    task_id: str
    payload: Dict[str, Any]
    priority: int

    @validator("payload")
    def validate_payload(cls, value):
        if "data" not in value or not isinstance(value["data"], list) or not value["data"]:
            raise ValueError("Payload must contain a non-empty 'data' list.")
        return value

# Example schema: TaskResult
class TaskResult(BaseModel):
    task_id: str
    success: bool
    result: Dict[str, Any]
