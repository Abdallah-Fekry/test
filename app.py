import streamlit as st

st.set_page_config(page_title="Love You Zuzu", page_icon="✨")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "first_log" not in st.session_state:
    st.session_state.first_log = True

home = st.Page("home.py", title='home')
login = st.Page("login.py")

if st.session_state.logged_in == False:
    pg = st.navigation([login], position='hidden')
if st.session_state.logged_in == True:
    pg = st.navigation([home], position='hidden')
# pg = st.navigation([home])
pg.run()
