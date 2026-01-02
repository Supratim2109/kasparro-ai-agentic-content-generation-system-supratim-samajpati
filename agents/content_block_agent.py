from agents.base_agent import BaseAgent
from core.task import Task

class ContentBlockAgent(BaseAgent):

    def __init__(self):
        self.blocks = {}

    def can_handle(self, task):
        return task.type in ["PRODUCT_NORMALIZED", "QA_GENERATED"]

    def handle(self, task):

        if task.type == "PRODUCT_NORMALIZED":
            p = task.payload
            self.blocks["benefits"] = p.get("Benefits", "")
            self.blocks["usage"] = p.get("How to Use", "")
            self.blocks["ingredients"] = p.get("Key Ingredients", "")
            self.blocks["price"] = p.get("Price", "")

        if task.type == "QA_GENERATED":
            self.blocks["faq"] = task.payload
            
        if {"benefits", "usage", "ingredients", "price", "faq"}.issubset(self.blocks.keys()):
            return [
                Task("CONTENT_BLOCKS_READY", self.blocks.copy())
            ]

        return []
