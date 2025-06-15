### 🗂️ Directory Structure

```
MultiProdigy/
├── agents/
├── bus/
├── config/
├── logging/
├── plugins/
├── runtime/
├── schemas/
├── support/
├── util/
├── __init__.py
```

---

## 🧠 Core Concepts

### 🔹 Agents (`agents/`)

This folder contains all agent definitions.

* **agent\_base.py**
  Defines the `BaseAgent` and high-level `Agent` class. All agents inherit from `BaseAgent`.

* **echo\_agent.py**
  Sample agent that echoes back any message it receives.

* **memory\_agent.py**
  Stores received messages in memory.

* **ollama\_agent.py**
  Runs LLM queries using the local Ollama CLI (e.g., Tinylama).

* **task\_manager.py**
  Manages agent configurations, goals, and orchestration logic.

* **user\_agent.py**
  Represents a human-like user agent that sends messages into the system.

---

### 🔹 Bus (`bus/`)

Message delivery infrastructure.

* **bus.py**
  A synchronous message dispatcher using a queue. Publishes, registers, and delivers messages to agents.

* **message\_bus.py**
  Alternative, lightweight message delivery system with direct dispatch.

---

### 🔹 Config (`config/`)

* **config.py**
  Loads application settings (e.g., logging levels) via Pydantic models.

---

### 🔹 Logging (`logging/`)

* **logger.py**
  Configures global logging behavior. Respects settings from `config.py`.

---

### 🔹 Runtime (`runtime/`)

Centralized engine that ties agents and bus together.

* **engine.py**
  Initializes agents and connects them to the message bus.

* **registry.py**
  Global static agent registry for lookup.

* **runtime.py**
  Instantiates agents and the bus, and registers everything.

* **scheduler.py**
  Background task scheduler to run periodic agent tasks.

---

### 🔹 Schemas (`schemas/`)

Pydantic-based validation and interface contracts.

* **message.py**
  Defines `Message`, the core communication object used between agents.

* **agent\_config.py**
  Defines configuration schema for agents.

* **agent\_interface.py**
  Abstract base class for agents that implement `handle_message`.

* **schemas.py**
  Convenience re-exports of common schemas.

---

### 🔹 Support (`support/`)

Utilities and health checks.

* **error.py**
  Custom exceptions related to agents and messages.

* **health.py**
  Health check status report (e.g., memory, Ollama availability).

* **matrices.py**
  Utility to generate identity matrices (for testing purposes).

---

### 🔹 Util (`util/`)

Currently empty. Use for any general-purpose tools/helpers.
