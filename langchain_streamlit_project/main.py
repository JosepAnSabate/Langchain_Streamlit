import langchain_helper as lch
import langchain_lawyer as lcl
import streamlit as st

import os
import openai
from dotenv import load_dotenv


load_dotenv()

st.sidebar.title("Choose your agent")
st.sidebar.info(
    "Each agent it is especialized in a different task. Choose the one that fits your needs."
)
# Define the tabs and their corresponding content
tabs = ["Names Generator", "Lawyer Agent", "Chat Agent"]
selected_tab = st.sidebar.radio("Select the agent", tabs)
st.sidebar.markdown("Ask to the agent whatever you want.")
# Define the button to click
def click_button():
    st.session_state.clicked = True

# Display the selected tab's content
if selected_tab == "Names Generator":
    st.title("Names Generator")
    user_company_type = st.selectbox(
        "What type of company do you want to name?",
        ("wine cellar", "coffee shop", "tech startup")
    )

    if user_company_type == "Wine cellar":
        feelings = st.text_area(
            "what feelings or ideas do you want to convey the wine cellar?", 
            max_chars=100)
    elif user_company_type == "cofee shop":
        feelings = st.text_area(
            "what feelings or ideas do you want to convey the coffe shop?", 
            max_chars=100)
    else:
        feelings = st.text_area(
            "what feelings or ideas do you want to convey the tech startup?", 
            max_chars=100)
    #submit botton
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    st.button('Submit', on_click=click_button)
    if st.button and feelings:
        response = lch.generate_name(user_company_type, feelings)
        st.text(response['company_name'])
    elif st.session_state.clicked:
        st.write("Please, fill the field")
    

elif selected_tab == "Lawyer Agent":
    st.header("Lawyer Agent")
    user_country = st.text_area(
        "Wich is your country? :earth_africa:", 
        max_chars=30, height=10, # default and min 30px
        placeholder="Argentina"
    )
    user_question = st.text_area(
        "What is your question?", 
        placeholder="Is legal to steal?",
        max_chars=300
    )

    #submit botton
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    st.button('Submit', on_click=click_button)
    if st.button and user_country and user_question:
        response = lcl.generate_law_res(user_country, user_question)
        st.write(response['text'])
    elif st.session_state.clicked:
        st.write("Please, fill the fields")
    
elif selected_tab == "Chat Agent":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages], stream=True):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})