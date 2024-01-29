import langchain_helper as lch
import streamlit as st

st.title('Pets name generator')

user_animal_type = st.sidebar.selectbox("What is your pet?", ("Cat","Dog","Horse"))

if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area("What color is your cat?", max_chars=15)
elif user_animal_type == "Dog":
    pet_color = st.sidebar.text_area("What color is your dog?", max_chars=15)
elif user_animal_type == "Horse":
    pet_color = st.sidebar.text_area("What color is your horse?", max_chars=15)

if pet_color: 
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name'])