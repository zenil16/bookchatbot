import streamlit as st
from chatbot import response

def fetch_conversation_history():
    if 'messages' not in st.session_state:
        st.session_state['messages'] =[
             {"role": "system", "content": "You are a BookGPT - You have all the knowledge about the book world. You know the book titles and the author. Answer any questions that the user asks about books in 100 words or less."}
        ]
    return st.session_state['messages']

st.title("BookGPT - Virtual Books Assistant")

user_input = st.chat_input("you: ")

if user_input:
    messages = fetch_conversation_history()
    messages.append({"role": "user", "content": user_input})
    answer = response(messages)
    messages.append({"role": "assistant", "content": answer})

    for message in messages:
        if message["role"] == "assistant":
            st.write(f"BookGPT: {message['content']}")
        elif message["role"] == "user":
            st.write(f"you: {message['content']}")
        
