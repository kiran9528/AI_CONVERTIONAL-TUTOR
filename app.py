import google.generativeai as genai
import streamlit as st

with open("keys/gemini_API_key.txt") as f:
    key = f.read()
genai.configure(api_key=key)

st.title("🗨️🤖AI Conversational Tutor")

st.chat_message("ai").write("Hi, How may I help you today?")

user_input = st.chat_input()

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="""You are a helpful AI Assistant who answers all the user queries politely.
                              If someone asks your name, tell them that your name is Chitti the Robot.""")

if "memory" not in st.session_state:
    st.session_state["memory"] = []

chat = model.start_chat(history=st.session_state['memory'])

for message in chat.history:
    st.chat_message(message.role).write(message.parts[0].text)

if user_input:
    st.chat_message("user").write(user_input)
    response = chat.send_message(user_input)
    st.chat_message("ai").write(response.text)
    st.session_state["memory"] = chat.history
