from fastapi import FastAPI
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

class Product(BaseModel):
    description: str
    quantity: int


@app.get("/")
def home():
    return {
        "message": "Rayeeva AI Internship Assignment API",
        "docs": "Open /docs to test the API endpoints"
    }

@app.post("/generate-category")
def generate_category(product: Product):

    description = product.description.lower()

    if "bamboo" in description or "reusable" in description:
        category = "Eco Products"
        sub_category = "Reusable Items"
        seo_tags = ["eco friendly", "plastic free", "sustainable", "green product"]
        filters = ["plastic-free", "recyclable", "eco-friendly"]

    elif "phone" in description or "smartphone" in description:
        category = "Electronics"
        sub_category = "Devices"
        seo_tags = ["smartphone", "electronics", "mobile device"]
        filters = ["brand", "price", "battery"]

    elif "shirt" in description or "cotton" in description:
        category = "Fashion"
        sub_category = "Clothing"
        seo_tags = ["fashion", "clothing", "apparel"]
        filters = ["size", "color", "brand"]

    else:
        category = "General"
        sub_category = "Other Products"
        seo_tags = ["product"]
        filters = ["price"]

    response = {
        "category": category,
        "sub_category": sub_category,
        "seo_tags": seo_tags,
        "filters": filters
    }

    logging.info(f"Prompt: {product.description}")
    logging.info(f"Response: {response}")

    return response


@app.post("/impact-report")
def impact_report(product: Product):

    plastic_saved = product.quantity * 0.2
    carbon_avoided = product.quantity * 0.3

    response = {
        "plastic_saved_kg": plastic_saved,
        "carbon_avoided_kg": carbon_avoided,
        "impact_statement": "This order reduces plastic waste and carbon emissions."
    }

    logging.info(f"Impact request: {product.description}")
    logging.info(f"Impact response: {response}")

    return response