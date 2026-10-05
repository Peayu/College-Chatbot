import streamlit as st 
from Chatbot import search
st.title("College FAQ Chatbot")
#initializing message directory
if "messages" not in st.session_state:
    st.session_state.messages = [        {
            "role": "assistant",
            "content": "Hi there! I'm your trusty college helper chatbot. Ask me any college-related question."
        }]

#printing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


#Getting input
prompt = st.chat_input("What do you want to know")
if prompt :
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = search(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role":  "assistant", "content" : response})

     
