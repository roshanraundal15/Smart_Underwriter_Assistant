# app2.py (AI Chat Underwriter)
import streamlit as st
from utils.gemini_chat_engine import chat_with_gemini

# Set page layout
st.set_page_config(page_title="AI Underwriter Chat", layout="centered")

# Title
st.title("🤖 AI Underwriter Chat")
st.markdown("Ask questions related to **insurance**, **health risk**, or **underwriting**.")

# Input field and send button
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("🗨️ Your Question", key="user_input")
    submit = st.form_submit_button("📤 Send")

# Output box
if submit and user_input:
    with st.spinner("Thinking..."):
        response = chat_with_gemini(user_input, [{"role": "user", "content": user_input}])

    st.markdown("### 🧑 You")
    st.markdown(user_input)

    st.markdown("### 🤖 Underwriter")
    if "I'm here to help with underwriting" in response:
        st.markdown(f"*{response}*")  # Italicized response for off-topic queries
    else:
        st.markdown(response)
