import streamlit as st
import asyncio
# import os
# import getpass
# import time
from chatbot_helper import send_chatbot_request
from llama_index.core.llms import ChatMessage
# from pinecone import Pinecone
# from llama_index.llms.groq import Groq
# from semantic_router.encoders import HuggingFaceEncoder

st.title("🤖 Welcome in :blue[_fam_ _property_] ChatBot :sunglasses:")

# index_name = "fam-rag"
# docs = []strealit 
# history_docs = []

# encoder = HuggingFaceEncoder(name="dwzhu/e5-base-4k")

# groq_client = Groq(api_key="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")
# st.secrets['REPLICATE_API_TOKEN']
# llm = Groq(model="llama3-70b-8192", api_key=st.secrets["GROQ_API_KEY"])

# configure client
# pc = Pinecone(api_key=st.secrets["PINECONE_API_KEY"])

# index = pc.Index(index_name)
# time.sleep(1)


# def onclickQuestion(question):
#     st.session_state.messages.append(ChatMessage(role= "user", content=question))
#     generate_llm(question)
    
def generate_llm(text):
    resp =  asyncio.run(send_chatbot_request(text,st.secrets["COHERE_API_KEY"]))
    print(resp) 
    
    # with st.chat_message("assistant"):
    #     st.write(resp)
    
    st.session_state.messages.append(ChatMessage(role= "assistant", content= resp))





# Call the API with an empty string to retrieve questions
    
# def get_questions(message: str):
#     return asyncio.run(question_suggestion_api(message))
# questions = question_suggestion_api("")

@st.dialog("Sign Up")
def email_form():
    email = st.text_input("Name")
    password = st.text_input("Password")
    print(password)
    print(email)
    
    if st.button('submit') and email == "admin" and password == "admin":
        st.session_state.messages.append(ChatMessage(role= "user", content="signing in"))
        st.session_state.messages.append(ChatMessage(role= "assistant", content="Thanks for signing in. you can complete :smile:"))
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = [
        ChatMessage(role="system", content="You are a real state assistant that helps users find best properties in Dubai that fit there requirement")
]        

if len(st.session_state.messages) == 7:
    st.write("please sign in to fam property to complete conversation")
    st.button('Sign In',on_click=email_form)
        
else:


            
    prompt = st.chat_input("Ask a question?")


    # Display the existing chat messages via `st.chat_message`.

                # if placeholder.button(question):
                #     prompt = question
    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.



    # print(len(st.session_state.messages))
    # if len(st.session_state.messages) > 1 or prompt:
        
        # with st.container(height=450):
                        
    if prompt:
        
        # with st.chat_message("user"):
        #     st.markdown(prompt)
        
        st.session_state.messages.append(ChatMessage(role= "user", content=prompt))
        generate_llm(prompt)
    
    for message in st.session_state.messages:
        if message.role != "system":
            with st.chat_message(message.role):
                st.markdown(message.content)


    # if st.session_state.messages[-1].role == 'assistant' or len(st.session_state.messages) == 1:

    #     print(st.session_state.messages[-1].content)
    #     print(st.session_state.messages[-1].role == 'assistant')
        
    #     if len(st.session_state.messages) == 1:
    #         questions = get_questions("")
    #     else:
    #         questions = get_questions(st.session_state.messages[-1].content)

    #     if questions:
    #         # Create an empty container to position the buttons
    #         placeholder = st.container(height=200)

    #         # Dynamically create buttons for each question
    #         for index,question in enumerate(questions):
    #             placeholder.button(question,key=index,on_click=lambda q=question: onclickQuestion(q))
                
    # print(questions)
    # print(st.session_state.messages)
                

    # Store and display the current prompt.    

    # Generate a response using the OpenAI API.
    # stream = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": m["role"], "content": m["content"]}
    #         for m in st.session_state.messages
    #     ],
    #     stream=True,
    # ) 
    
    
    # if not prompt.__contains__("Yes") or not prompt.__contains__("No"):
    #     docs = oracle_db(prompt, 5)
    #     if len(history_docs) == 3:
    #         history_docs.pop(0) 
    #         history_docs.append(docs)
    #         print(history_docs)
    #         print(len(history_docs))
    #     else:
    #         history_docs.append(docs)
    #         print(history_docs)
    #         print(len(history_docs))
            
            

        # result = generate(prompt, docs, groq_client, st.session_state.messages)

    # docs = "\n---\n".join([str(i) for doc in history_docs for i in doc ])
    
    # system_message =f'''
    #     You are a real state assistant and agent act as that and help users find best properties and there transition in Dubai that fit there requirement using the
    #     context and chat history provided below. 
    #     please be precise when you answer the user with Full specifications and details and get the answer from your history if the question is not related to the context.
    #     if you ask the user a yes/no question do not use the provided context for response, use chat history for answer instead.
    
    #     if the context or the chat history may not have the answer of the question get the answer from chat history if not related please
    #     ask user to provide you more information
    #     \n\n
    #     CONTEXT:\n
    #     {docs}
    #     '''
    # for i, k in enumerate(st.session_state.messages):
    #     if k.role =="system":
    #         st.session_state.messages[i].content = system_message

        

    # generate response
    # chat_response = groq_client.chat.completions.create(
    #     model="llama3-70b-8192",
    #     messages=[
    #         {"role": m["role"], "content": m["content"]}
    #         for m in st.session_state.messages
    #     ],
    #     stream=True
    # )
    # resp = llm.stream_chat(st.session_state.messages)
        # resp =  asyncio.run(send_chatbot_request(prompt,st.secrets["COHERE_API_KEY"]))
    
    # print(st.session_state.messages)

    # Stream the response to the chat using `st.write_stream`, then store it in 
    # session state.
    # print(resp)
        
        # print(resp)   
    
        # with st.chat_message("assistant"):
        #     st.write(resp)
        
        # st.session_state.messages.append(ChatMessage(role= "assistant", content= resp))
