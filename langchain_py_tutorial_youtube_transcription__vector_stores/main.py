import streamlit as st
import langchain_helper as lch
import textwrap

st.title('Youtube Assistant')

with st.sidebar:
    with st.form(key='form'):
        #video_url = 'https://www.youtube.com/watch?v=t9DNBxpvxs0'
        youtube_url = st.sidebar.text_area(
            label="Video URL",
            max_chars=100, 
            height=150
        )
        query = st.sidebar.text_area(
            label="Ask me about the video",
            key='query',
            max_chars=100, 
            height=150
        )
        
        submit_button = st.form_submit_button(
            label='Submit'
        )
    
if query and youtube_url:
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    #st.text( dir(db))
    response = lch.get_response_from_query(db, query)
    st.subheader('Answer:')
    st.text(textwrap.fill(response, width=100))

