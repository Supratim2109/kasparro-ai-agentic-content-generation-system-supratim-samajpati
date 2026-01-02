from agents.base_agent import BaseAgent
from core.task import Task

class AnswerAgent(BaseAgent):

    def can_handle(self, task):
        return task.type == "QUESTION_GENRATED"
    
    def handle(self, task):
        qa_pairs=[]

        for q in task.payload:
            qa_pairs.append({
                "question": q["question"],
                "answer":"Derived from product data",
                "category": q["category"]
            })
        return [
            Task("QA_GENERATED", qa_pairs)
        ]