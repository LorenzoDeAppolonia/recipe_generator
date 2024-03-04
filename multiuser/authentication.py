import streamlit as st
from st_pages import Page, show_pages, add_page_title
from recipe_llm import final_chain
from .get_authenticator import get_authenticator


def user_registration(authenticator):
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(
            preauthorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)


def user_login(authenticator):
    authenticator.login()
    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f'Welcome *{st.session_state["name"]}*')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')





