from abc import ABC, abstractmethod  # Importing modules to support abstract base classes and async operations
import asyncio  # Importing asyncio for asynchronous programming features like sleep

# Defining an abstract base class for agents
class Agent(ABC):
    # Abstract method that should be implemented to start the agent
    @abstractmethod
    async def start(self): ...
    
    # Abstract method that should be implemented to stop the agent
    @abstractmethod 
    async def stop(self): ...
    
    # Abstract method to handle incoming messages, expected to receive a dictionary
    @abstractmethod
    async def handle(self, message: dict): ...
    
    # Abstract method for the agent's main processing logic
    @abstractmethod
    async def process(self): ...
    
    # Optional helper method for sleeping (pausing execution) for a given number of seconds
    async def sleep(self, seconds: float):
        """Default sleep implementation"""
        await asyncio.sleep(seconds)
    
    # Optional helper method to terminate the agent by calling its stop method
    async def terminate(self):
        """Default termination"""
        await self.stop()
