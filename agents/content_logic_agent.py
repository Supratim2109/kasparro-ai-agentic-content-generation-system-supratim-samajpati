class ContentLogicAgent:
    def run(self, product_model:dict,comparison_product:dict=None)-> dict:
        blocks={
            "benefits_block":product_model["benefits"],
            "ingredients_block":product_model["ingredients"],
            "usage_block":product_model["usage"],
            "safety_block":product_model["side_effects"],
            "price_block":product_model["price"]
        }

        if comparison_product:
            blocks["comparison_block"] = {
                "price": (
                    f"{product_model['name']} is more affordable than {comparison_product['name']}."
                    if product_model["price"] < comparison_product["price"]
                    else f"{comparison_product['name']} is more affordable than {product_model['name']}."
                ),
                "ingredients": (
                    f"{product_model['name']} contains {', '.join(product_model['ingredients'])}, "
                    f"while {comparison_product['name']} contains {', '.join(comparison_product['ingredients'])}."
                ),
                "benefits": (
                    f"{product_model['name']} focuses on {', '.join(product_model['benefits'])}, "
                    f"while {comparison_product['name']} focuses on {', '.join(comparison_product['benefits'])}."
                )
            }
        return blocks