import streamlit as st
from think_heal_grow import create_chatbot  # your chatbot logic
from history_manager import save_history

st.set_page_config(page_title="Think Heal Grow", layout="centered")
st.title("🧠 AI Psychological Counseling Chatbot")

# Initialize session state
if "chatbot" not in st.session_state:
    st.session_state.chatbot = create_chatbot()
    st.session_state.chat_history = []

# 🧹 Clear Chat Button
if st.button("🧹 Clear Chat"):
    st.session_state.chatbot = create_chatbot()  # Reset bot with fresh memory
    st.session_state.chat_history = []
    st.success("Chat cleared.")

# Intro Message
st.markdown("""
💬 _This chatbot simulates a conversation with a  clinical psychologist._  
_Not a substitute for real therapy._
""")

# User Input
user_input = st.text_input("You:", placeholder="How are you feeling today?")

# Handle User Input
if user_input:
    response = st.session_state.chatbot.run(user_input)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Therapist", response))

    save_history(st.session_state.chat_history)

# Display Chat History
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧍‍♂️ You:** {msg}")
    else:
        st.markdown(f"**🧑‍⚕️ Therapist:** {msg}")
