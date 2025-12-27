# agents/question_generator_agent.py

class QuestionGeneratorAgent:
    KNOWLEDGE_BASE = {
        "Informational": [
            "What is {product_name}?",
            "What are the main benefits of {product_name}?",
            "Who should use {product_name}?"
        ],
        "Usage": [
            "How should {product_name} be used?",
            "When should {product_name} be applied?",
            "How many drops of {product_name} should be used?"
        ],
        "Safety": [
            "Does {product_name} have any side effects?",
            "Is {product_name} suitable for sensitive skin?",
            "Can {product_name} cause irritation?"
        ],
        "Ingredients": [
            "What are the key ingredients in {product_name}?",
            "Does {product_name} contain Vitamin C?",
            "Does {product_name} contain Hyaluronic Acid?"
        ],
        "Pricing": [
            "What is the price of {product_name}?",
            "Is {product_name} affordable?",
            "Is {product_name} worth its price?"
        ]
    }

    def rule_applicable(self, category: str, product_model: dict) -> bool:
        if category == "Usage":
            return bool(product_model.get("usage"))
        if category == "Safety":
            return bool(product_model.get("side_effects"))
        if category == "Ingredients":
            return bool(product_model.get("ingredients"))
        if category == "Pricing":
            return bool(product_model.get("price"))
        return True 

    def run(self, product_model: dict) -> list:
        questions = []

        for category, templates in self.KNOWLEDGE_BASE.items():
            if self.rule_applicable(category, product_model):
                for template in templates:
                    questions.append({
                        "question": template.format(
                            product_name=product_model["name"]
                        ),
                        "category": category
                    })

        return questions
