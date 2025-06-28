# utils/gemini_chat_engine.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not set in environment variables.")
genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat_session = model.start_chat(history=[])

# 🔍 Simple relevance filter
def is_insurance_related(query):
    keywords = [
        "insurance", "risk", "health", "diabetes", "smoking", "premium",
        "underwriting", "age", "bmi", "medical", "affordability", "coverage", "policy"
    ]
    query_lower = query.lower()
    return any(word in query_lower for word in keywords)

def chat_with_gemini(prompt: str, history=[]):
    """
    Handles relevance and then calls Gemini.
    """
    if not is_insurance_related(prompt):
        return (
            "🤖 I'm here to help with underwriting, insurance, and health-related questions.\n"
            "Try asking about your risk score, premium affordability, or medical profile!"
        )
    try:
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini API Error: {str(e)}"
