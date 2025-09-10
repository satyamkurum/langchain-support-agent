import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    """Initialize Gemini LLM"""
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.3
    )
