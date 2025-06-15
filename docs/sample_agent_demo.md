# Demo: MultiProdigy Echo Conversation

This `demo/` directory shows a minimal example of how to use the **MultiProdigy** framework to have two agents talk.

## Files

- **echo_agent.py**  
  Implements `EchoAgent`, which listens for messages, prints their contents, and replies with `Echo: <content>`.

- **user_agent.py**  
  Implements `UserAgent`, which can send a greeting and prints any replies it receives.

- **demo.py**  
  Orchestrates the conversation:
  1. Creates a shared `MessageBus`
  2. Registers `EchoAgent` and `UserAgent`
  3. Has `UserAgent` send “Hello, MultiProdigy!” to `EchoAgent`

## Prerequisites

- Python 3.8+  
- Your project layout must be:
```
your-project/
├── MultiProdigy/    ← core framework package
└── demo/            ← this folder
```

- Run demos from the **project root** so that Python finds `MultiProdigy`:

```bash
cd /path/to/your-project
python demo/demo.py
````

## Usage

1. From the project root, invoke:

   ```bash
   python demo/demo.py
   ```
2. You should see output similar to:

   ```
   🚀 Starting Echo Agent Demo...

   [bus] registered agent EchoAgent
   [bus] registered agent UserAgent
   [bus] publishing ▶ UserAgent → EchoAgent: Hello, MultiProdigy!
   [bus] dequeued ▶ UserAgent → EchoAgent: Hello, MultiProdigy!
   [bus] delivering to EchoAgent
   [EchoAgent] Received: Hello, MultiProdigy!
   [bus] publishing ▶ EchoAgent → UserAgent: Echo: Hello, MultiProdigy!
   [bus] dequeued ▶ EchoAgent → UserAgent: Echo: Hello, MultiProdigy!
   [bus] delivering to UserAgent
   [UserAgent] Received: Echo: Hello, MultiProdigy!
   ```

## Quick Start Guide

* **Add a new agent**: subclass `BaseAgent`, implement `on_message()`, call `self.bus.publish()` to reply.
* **Register** it in `demo.py` with `bus.register(your_agent)`.
* **Trigger** interactions via `agent.send()` or custom helper methods.
