import streamlit as st
import datetime

col1, col2 = st.columns(2)
with col1:
    st.image("images/cherry blossom-amico.png")
with col2:
    st.write("---")
    # st.write("  \n")
    st.header("Login")
    st.write("Enter the best date ever ya zuzu")
    date = st.date_input("")
    bt = st.button("Login")
    st.write("---")
    if bt:
        if date == datetime.date(2021,6,25):
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("اخس عليكي اخس!")
    # st.switch_page(home)
