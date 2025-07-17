from abc import ABC, abstractmethod
from typing import List

class LLMClient(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        pass

    @abstractmethod
    def embed(self, texts: List[str], **kwargs) -> List[List[float]]:
        pass

    @abstractmethod
    def chat(self, messages: List[dict], **kwargs) -> str:
        pass
