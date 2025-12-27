import os
import json
from agents.orchestrator_agent import OrchestratorAgent

raw_product_data={
    "Product Name": "GlowBoost Vitamin C Serum",
    "Concentration": "10% Vitamin C",
    "Skin Type": "Oily, Combination",
    "Key Ingredients": "Vitamin C, Hyaluronic Acid",
    "Benefits": "Brightening, Fades dark spots",
    "How to Use": "Apply 2–3 drops in the morning before sunscreen",
    "Side Effects": "Mild tingling for sensitive skin",
    "Price": "₹699"
}

def main():
    orchestrator=OrchestratorAgent()
    outputs=orchestrator.run(raw_product_data)
    os.makedirs("outputs",exist_ok=True)

    with open("outputs/faq.json","w") as f:
        json.dump(outputs["faq_page"],f,indent=2)

    with open("outputs/product_page.json","w") as f:
        json.dump(outputs["product_page"],f,indent=2)

    with open("outputs/comparison_page.json", "w") as f:
        json.dump(outputs["comparison_page"],f,indent=2)

    print("Pipeline Executed Successfully")

if __name__=="__main__":
    main()