import heapq  # Heap queue algorithm for priority queue implementation

# Scheduler class to manage agents based on their priority
class PriorityScheduler:
    def __init__(self):
        self.tasks = []  # Internal priority queue (min-heap) to hold (priority, agent) tuples
    
    # Add an agent to the queue with its priority
    def add_agent(self, agent, priority: int):
        # Push a tuple (priority, agent) so agents with lower priority numbers run first
        heapq.heappush(self.tasks, (priority, agent))
    
    # Run the next agent in the priority queue
    async def run_next(self):
        if self.tasks:
            _, agent = heapq.heappop(self.tasks)  # Pop agent with highest priority (lowest number)
            await agent.process()  # Run the agent's async process method
