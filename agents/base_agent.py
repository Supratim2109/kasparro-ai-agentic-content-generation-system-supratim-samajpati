class BaseAgent:
    def can_handle(self, task)->bool:
        raise NotImplementedError
    def handle(self, task)->list:
        raise NotImplementedError
    
    