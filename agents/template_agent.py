from agents.base_agent import BaseAgent
from core.task import Task
from templates.faq_template import render_faq
from templates.product_template import render_product_page
from templates.comparison_template import render_comparison_page

class TemplateAgent(BaseAgent):

    def can_handle(self, task):
        return task.type == "CONTENT_BLOCKS_READY"

    def handle(self, task):
        blocks = task.payload
        tasks = []

        if "faq" in blocks:
            faq_page = render_faq(blocks)
            tasks.append(Task("PAGE_GENERATED", {
                "page_type": "faq",
                "content": faq_page
            }))

        if "benefits" in blocks:
            product_page = render_product_page(
                blocks,
                product_name="GlowBoost Vitamin C Serum"
            )
            tasks.append(Task("PAGE_GENERATED", {
                "page_type": "product",
                "content": product_page
            }))

        product_a = {
            "name": "GlowBoost Vitamin C Serum",
            "ingredients": ["Vitamin C", "Hyaluronic Acid"],
            "benefits": ["Brightening", "Fades dark spots"],
            "price": 699
        }

        product_b = {
            "name": "RadiantPlus Serum",
            "ingredients": ["Hyaluronic Acid"],
            "benefits": ["Hydration"],
            "price": 799
        }

        comparison_page = render_comparison_page(product_a, product_b)

        tasks.append(Task("PAGE_GENERATED", {
            "page_type": "comparison",
            "content": comparison_page
        }))

        return tasks
