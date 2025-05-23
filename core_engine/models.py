from pydantic import BaseModel  # Import BaseModel for data validation and parsing
from typing import Any

# Model representing a message exchanged between agents
class MessageModel(BaseModel):
    sender: str    # Identifier of the message sender
    receiver: str  # Identifier of the message receiver
    content: str   # The message content as a string

# ✅ Model representing a task request sent to an agent
class TaskRequest(BaseModel):
    input: Any      # Input can be any type depending on task
    task_type: str  # Type of task to perform

# ✅ Model representing the result of a task completed by an agent
class TaskResult(BaseModel):
    output: Any     # Output of the task
    success: bool   # Whether the task was successful
