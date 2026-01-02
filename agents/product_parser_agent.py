from agents.base_agent import BaseAgent
from core.task import Task

class ProductParserAgent(BaseAgent):
    def can_handle(self, task):
        return task.type== "PRODUCT_INPUT_RECEIVED"
    
    def handle(self, task):
        raw= task.payload

        product_model= {}
        for key,value in raw.items():
            product_model[key.strip()]=value.strip()

        return [
            Task("PRODUCT_NORMALIZED", product_model)
        ]