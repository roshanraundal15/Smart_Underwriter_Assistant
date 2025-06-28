import streamlit as st
from utils.gemini_chat_engine import chat_with_gemini

def live_chat():
    st.markdown("## 💬 Ask Our AI Underwriter")
    user_input = st.text_input("You:", key="user_input")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("Gemini is thinking..."):
            response = chat_with_gemini(user_input, st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "model", "content": response})

    for msg in st.session_state.chat_history:
        role = "🧑 You" if msg["role"] == "user" else "🤖 Gemini"
        st.markdown(f"**{role}:** {msg['content']}")
