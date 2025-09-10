# Customer Support Bot with LangChain and Gemini

This project implements a customer support assistant powered by LangChain and Google Gemini. It demonstrates how to build an AI agent that can handle FAQs, order tracking, and conversational context, with a simple Streamlit interface.

---

## Features

- **FAQ Lookup**: Fetches answers from a structured JSON knowledge base (`faq.json`).
- **Order Tracking**: Provides simulated order tracking responses.
- **Conversational Memory**: Maintains context across multiple user interactions.
- **LangChain Agent and Tools**: Extensible structure for adding more functionalities.
- **Streamlit Interface**: Simple and interactive frontend for end users.
- **Gemini Integration**: Uses Google Gemini through the `langchain-google-genai` integration.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/customer-support-bot.git
   cd customer-support-bot
   python -m venv venv
  
2. On Windows
   ```bash
   venv\Scripts\activate
   source venv/bin/activate
   ```


4. Install Requirements
   ```bash 
    pip install -r requirements.txt
   ```

5. Environment Setup
   ```bash
    GOOGLE_API_KEY=your_api_key
   ```  

6. Run
    ```bash
    streamlit run app.py



