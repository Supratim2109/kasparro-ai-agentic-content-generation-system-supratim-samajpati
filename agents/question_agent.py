from agents.base_agent import BaseAgent
from core.task import Task

class QuestionAgent(BaseAgent):
    KNOWLEDGE_BASE = {
        "Informational": [
            "What is {name}?",
            "What are the benefits of {name}?",
            "Who should use {name}?"
        ],
        "Usage": [
            "How should {name} be used?",
            "When should {name} be applied?",
            "How many drops of {name} should be used?"
        ],
        "Safety": [
            "Does {name} have side effects?",
            "Is {name} suitable for sensitive skin?",
            "Can {name} cause irritation?"
        ],
        "Pricing": [
            "What is the price of {name}?",
            "Is {name} affordable?",
            "Is {name} worth its price?"
        ],
        "Ingredients": [
            "What are the key ingredients in {name}?",
            "Does {name} contain Vitamin C?",
            "Does {name} contain Hyaluronic Acid?"
        ]
    }

    def can_handle(self, task):
        return task.type == "PRODUCT_NORMALIZED"
    
    def handle(self, task):
        product = task.payload
        name= product.get("Product Name","this product")

        questions=[]

        for category,template in self.KNOWLEDGE_BASE.items():
            for t in template:
                questions.append(
                    {
                        "question":t.format(name=name),
                        "category":category
                    }
                )
        return [
            Task("QUESTIONS_GENERATED", questions)
        ]
    