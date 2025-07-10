from abc import ABC, abstractmethod

class BaseLLMClient(ABC):
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """
        Generate text based on the given prompt.
        Must be implemented by subclasses.
        """
        pass
