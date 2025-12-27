class TemplateEngineAgent:
    def generate_faq_page(self,qa_pairs:list)-> dict:
        return {
            "page_type":"FAQ",
            "faqs":qa_pairs[:5]
        }
    def generate_product_page(self, product_model:dict, blocks:dict)-> dict:
        return {
            "product_name":product_model["name"],
            "ingredients":blocks["ingredients_block"],
            "benefits":blocks["benefits_block"],
            "usage":blocks["usage_block"],
            "side_effects":blocks["safety_block"],
            "price":blocks["price_block"]
        }
    def generate_comparison_page(self, product_a:dict,product_b:dict, blocks:dict) -> dict:
        return {
            "product_a":product_a["name"],
            "product_b":product_b["name"],
            "comparison":blocks["comparison_block"]
        }