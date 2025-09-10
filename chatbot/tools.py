import json
import os
from langchain.agents import Tool

# Load FAQ database
FAQ_PATH = os.path.join("data", "faq.json")
if os.path.exists(FAQ_PATH):
    with open(FAQ_PATH, "r") as f:
        faq_data = json.load(f)
else:
    faq_data = {
        "return policy": "You can return products within 30 days.",
        "shipping time": "Orders arrive in 3-5 business days.",
        "payment methods": "We accept credit card, UPI, and PayPal."
    }

def faq_lookup(query: str) -> str:
    for key, value in faq_data.items():
        if key in query.lower():
            return value
    return "Sorry, I couldn’t find that in FAQ."

def track_order(order_id: str) -> str:
    return f"Order {order_id} is in transit and will arrive in 2 days."

def get_tools():
    return [
        Tool(
            name="FAQ Lookup",
            func=faq_lookup,
            description="Answer FAQs like return policy, shipping time, etc."
        ),
        Tool(
            name="Order Tracker",
            func=track_order,
            description="Check order status when given an order ID."
        )
    ]
