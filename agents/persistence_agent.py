import os
import json
from agents.base_agent import BaseAgent

class ArtifactPersistenceAgent(BaseAgent):

    def __init__(self, output_dir="outputs"):
        self.output_dir=output_dir
        os.makedirs(self.output_dir,exist_ok=True)

    def can_handle(self, task):
        return task.type=="PAGE_GENRATED"
    
    def handle(self, task):
        page_type=task.payload["page_type"]
        content=task.payload["content"]

        filename_map={
            "faq": "faq.json",
            "product": "product_page.json",
            "comparison": "comparison_page.json"
        }

        filename=filename_map.get(page_type)

        if filename:
            path=os.path.join(self.output_dir, filename)
            with open(path,'w',encoding='utf-8') as f:
                json.dump(content,f, indent=2)
        return []