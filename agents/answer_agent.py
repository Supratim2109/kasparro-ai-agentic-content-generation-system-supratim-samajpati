from agents.base_agent import BaseAgent
from core.task import Task

class AnswerAgent(BaseAgent):

    def can_handle(self, task):
        return task.type == "QUESTIONS_GENERATED"

    def handle(self, task):
        qa_pairs = []

        for q in task.payload:
            category = q["category"]

            if category == "Informational":
                answer = "This product is designed to improve skin appearance and health."

            elif category == "Usage":
                answer = "It should be used as per the recommended usage instructions provided."

            elif category == "Safety":
                answer = "Some users may experience mild tingling, especially sensitive skin types."

            elif category == "Pricing":
                answer = "The product is priced competitively within its category."

            elif category == "Ingredients":
                answer = "The product contains carefully selected active ingredients."

            else:
                answer = "Information is derived from product data."

            qa_pairs.append({
                "question": q["question"],
                "answer": answer,
                "category": category
            })

        return [
            Task("QA_GENERATED", qa_pairs)
        ]
