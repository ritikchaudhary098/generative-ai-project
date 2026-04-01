import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

# Load environment variables
load_dotenv()

# Load model
model = ChatMistralAI(model="mistral-small-2603")

# Page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Built with LangChain + Mistral</p>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 👨‍💻 About")
    st.write("This chatbot is built using:")
    st.write("- LangChain")
    st.write("- Mistral AI")
    st.write("- Streamlit")

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response with loading spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            response = model.invoke(prompt)
            reply = response.content
            st.markdown(reply)

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": reply})