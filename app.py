import streamlit as st
from dotenv import load_dotenv
from chatbot.agent import get_agent

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Customer Support Bot", page_icon="🤖", layout="wide")

st.title("Customer Support Assistant")
st.write("Ask me about orders, shipping, payments, or return policy!")

# Initialize session state
if "agent" not in st.session_state:
    st.session_state.agent = get_agent()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
query = st.chat_input("Type your message here...")

if query:
    # Store user message
    st.session_state.chat_history.append(("user", query))

    # Get agent response
    response = st.session_state.agent.run(query)
    st.session_state.chat_history.append(("bot", response))

# Display conversation
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.chat_message("user").markdown(msg)
    else:
        st.chat_message("assistant").markdown(msg)
