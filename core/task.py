class Task:
    def __init__(self, task_type: str,payload:str):
        self.type=task_type
        self.payload=payload

    def __repr__(self):
        return f"Task(type={self.type})"