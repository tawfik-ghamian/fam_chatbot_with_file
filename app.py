import asyncio
import streamlit as st

from llama_index.core.llms import ChatMessage
from chatbot_helper import upload_file,chat,question_suggestion

if "upload" not in st.session_state:
    st.session_state.upload = "open"

def generate_llm(text):
    
    st.session_state.messages.append(ChatMessage(role= "user", content=text))
    msg = st.toast('Generating...')
    resp =  asyncio.run(chat(text)) 
    if resp.status_code == 200:
        # Parse the response JSON 
        st.session_state.messages.append(ChatMessage(role= "assistant", content= resp.json()["result"]["answer"]))
        msg.empty()
    else:
        msg.toast(resp.json()["message"])
    print("resp_llm ",resp)
    
def upload_file_api(file):
    msg = st.toast('Uploading file...')
    resp =  asyncio.run(upload_file(file)) 
    print("resp ", resp)
    msg.toast(resp)

st.markdown(
    r"""
    <style>
    #MainMenu {visibility: hidden;}
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True
)
    
st.title("🤖 Welcome in :blue[_fam_ _property_] ChatBot ")

if "messages" not in st.session_state:
    st.session_state.messages = [
        ChatMessage(role="system", content="")
]        
prompt = st.chat_input("Ask a question?")
    
uploaded_file = st.sidebar.file_uploader("Upload a file", type=["docx","pdf"])

if uploaded_file is not None and prompt is None and "upload" in st.session_state and st.session_state.upload == "open":
    
    upload_file_api(file=uploaded_file)
    uploaded_file.close()
    st.session_state.upload = "close"

if prompt:
    # Generate suggestion question only if no file uploaded or file is closed

    # Generate LLM response based on prompt
    generate_llm(prompt)

for message in st.session_state.messages:
    if message.role != "system":
        with st.chat_message(message.role):
            st.markdown(message.content)
