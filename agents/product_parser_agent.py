class ProductParserAgent:
    def run(self, raw_product_data:dict) -> dict:
        return{
            "name":raw_product_data["Product Name"],
            "concentration":raw_product_data["Concentration"].split()[0],
            "skin_type": [s.strip() for s in raw_product_data["Skin Type"].split(",")],
            "ingredients":[i.strip() for i in raw_product_data["Key Ingredients"].split(",")],
            "benefits":[b.strip() for b in raw_product_data["Benefits"].split(",")],
            "usage": raw_product_data["How to Use"],
            "side_effects":raw_product_data["Side Effects"],
            "price": int(raw_product_data["Price"].replace("₹", ""))
        }