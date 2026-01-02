from collections import deque

class MessageBus:
    def __init__(self):
        self.queue=deque()

    def publish(self,task):
        self.queue.append(task)
    
    def has_tasks(self):
        return len(self.queue)>0
    
    def next_task(self):
        return self.queue.popleft()
    