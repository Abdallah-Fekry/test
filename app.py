import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

home = st.Page("home.py", title='home')
login = st.Page("login.py")

if st.session_state.logged_in == False:
    pg = st.navigation([login], position='hidden')
if st.session_state.logged_in == True:
    pg = st.navigation([home], position='hidden')
# pg = st.navigation([home])
pg.run()