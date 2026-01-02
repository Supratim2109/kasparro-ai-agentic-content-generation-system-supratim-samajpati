from agents.base_agent import BaseAgent
from core.task import Task

class ContentBlockAgent(BaseAgent):
    def can_handle(self, task):
        return task.type in ["PRODUCT_NORMALIZED", "QA_GENERATED"]
    def handle(self, task):
        blocks= {}

        if task.type=="PRODUCT_NORMALIZED":
            p = task.payload
            blocks["benefits"] = p.get("Benefits", "")
            blocks["usage"] = p.get("How to Use", "")
            blocks["ingredients"] = p.get("Key Ingredients", "")
            blocks["price"] = p.get("Price", "")
        
        if task.type=="QA_GENERATED":
            blocks['faq']=task.payload
        return [
            Task("CONTENT_BLOCKS_READY", blocks)
        ]