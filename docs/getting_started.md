# 🚀 Getting Started

### ✅ 1. Install Dependencies

Ensure you have Python 3.9+ and the following installed:

```bash
pip install -r requirements.txt
```

If using Ollama:

```bash
ollama run tinylama
```

---

### ✅ 2. Run the Demo

If you're using the `demo/` directory (outside `MultiProdigy/`):

Update the `PYTHONPATH` or use dynamic path insert:

```python
# Add to top of demo.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'MultiProdigy')))
```

Then run:

```bash
python demo/demo.py
```

---

## 🔧 Custom Agent Example

```python
from MultiProdigy.agents.agent_base import BaseAgent
from MultiProdigy.schemas.message import Message

class MyAgent(BaseAgent):
    def receive_message(self, message: Message):
        print(f"MyAgent got: {message.content}")
```

---

## 📌 Notes

* Agents **must be registered** to the bus to receive messages.
* `MessageBus` supports **pub-sub-like dispatch** via name-based routing.
* Agents use either `receive_message` or `handle_message` depending on context.
