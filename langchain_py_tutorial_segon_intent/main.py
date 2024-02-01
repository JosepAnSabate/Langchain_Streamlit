import langchain_helper as lch
import streamlit as st


st.title('Company Name Generator')


company_type = st.sidebar.selectbox("What's your company type?",                                
         ['AI', 'Architecture', 'Marketing'])

if company_type == 'AI':
    values = st.sidebar.multiselect("What are your company values?",
         ['transparency', 'ethics', 'privacy'])
elif company_type == 'Architecture':
    values = st.sidebar.multiselect("What are your company values?",
         ['sustainability', 'innovation', 'creativity']
         )
elif company_type == 'Marketing':
    values = st.sidebar.text_area(label="What are your company values?",
         max_chars=100, height=150)
    
if st.sidebar.button('Generate'):
    response = lch.generate_company_names(company_type, values)
    
    st.write(response['company_name'])