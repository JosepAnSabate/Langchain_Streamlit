import streamlit as st

st.title("Session State Basics")

"st.session_state object: ", st.session_state

# widgets 
number = st.slider("Pick a number", 0, 10, 1, key="my_number")

st.write(st.session_state)

col1, buff, col2 = st.columns([1, 0.5, 3])

option_names = ["a", "b", "c"]

next = st.button("Next option")

if next:
    if st.session_state.radio_option == "a":
        st.session_state.radio_option = "b"
    elif st.session_state.radio_option == "b":
        st.session_state.radio_option = "c"
    else:
        st.session_state.radio_option = "a"

option = col1.radio("Pick an option", option_names, key="radio_option")

if option == "a":
    col2.write("You selected option a")
elif option == "b":
    col2.write("You selected option b")
else:
    col2.write("You selected option c")