# agents/answer_generator_agent.py

class AnswerGeneratorAgent:
    ANSWER_KNOWLEDGE_BASE = {
        "Informational": lambda p: (
            f"{p['name']} is a skincare product designed to help with "
            f"{', '.join(p['benefits'])}."
        ),
        "Usage": lambda p: p["usage"],
        "Safety": lambda p: (
            f"{p['name']} may cause {p['side_effects'].lower()}."
        ),
        "Ingredients": lambda p: (
            f"The key ingredients in {p['name']} are "
            f"{', '.join(p['ingredients'])}."
        ),
        "Pricing": lambda p: (
            f"The price of {p['name']} is ₹{p['price']}."
        )
    }

    def run(self, product_model: dict, questions: list) -> list:
        qa_pairs = []

        for q in questions:
            category = q["category"]
            answer_rule = self.ANSWER_KNOWLEDGE_BASE.get(category)
            if not answer_rule:
                continue
            qa_pairs.append({
                "question": q["question"],
                "answer": answer_rule(product_model),
                "category": category
            })
        return qa_pairs
