def render_comparison_page(product_a, product_b):
    return {
        "product_a": product_a,
        "product_b": product_b,
        "comparison": {
            "price": (
                f"{product_a['name']} is more affordable than {product_b['name']}"
                if product_a["price"] < product_b["price"]
                else f"{product_b['name']} is more affordable than {product_a['name']}"
            ),
            "ingredients": (
                f"{product_a['name']} contains {', '.join(product_a['ingredients'])}, "
                f"while {product_b['name']} contains {', '.join(product_b['ingredients'])}"
            ),
            "benefits": (
                f"{product_a['name']} focuses on {', '.join(product_a['benefits'])}, "
                f"while {product_b['name']} focuses on {', '.join(product_b['benefits'])}"
            )
        }
    }
