from MultiProdigy.llm.base import BaseLLMClient

# 🧪 Simulated OpenAI Client
class OpenAIClient(BaseLLMClient):
    async def generate(self, prompt: str) -> str:
        return f"Simulated response from OpenAI for: {prompt}"


# 🧪 Simulated Gemini Client
class GeminiClient(BaseLLMClient):
    async def generate(self, prompt: str) -> str:
        return f"Simulated response from Gemini for: {prompt}"


# ✅ Real Ollama Client (Offline)
import subprocess

class OllamaClient(BaseLLMClient):
    def __init__(self, model: str = "tinyllama"):
        self.model = model

    async def generate(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                ["ollama", "run", self.model],
                input=prompt.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=60,
            )
            return result.stdout.decode().strip()
        except Exception as e:
            return f"❌ Ollama Error: {str(e)}"
