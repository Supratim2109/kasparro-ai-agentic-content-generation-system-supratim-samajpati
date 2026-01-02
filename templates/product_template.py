def render_product_page(blocks, product_name):
    return {
        "product_name": product_name,
        "benefits": blocks["benefits"],
        "usage": blocks["usage"],
        "ingredients": blocks["ingredients"],
        "price": blocks["price"]
    }
