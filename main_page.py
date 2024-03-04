import streamlit as st
from st_pages import Page, show_pages


st.title('SouschefAI :female-cook:')
st.subheader(f'What should we cook today?')

show_pages(
    [
        Page("main_page.py", "Home", ":house:"),
        Page("recipe_search.py", "Cerca ricetta", ":mag:"),
        Page("user_recipe_display.py", "Ricettario", ":books:"),
    ]
)

st.divider()
st.subheader('Find the recipe that suits you')

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/asparagus-2169305_1280.jpg")

with col2:
    st.image("images/salmon-518032_1280.jpg")

with col3:
    st.image("images/stir-fried-fish-with-sweet-chili-906248_1280.jpg")

st.divider()

st.subheader("Add the recipe to your personal cookbook")
# login = st.button('Login/Logout')
# register = st.button('Register')
# authenticator = get_authenticator()
#
# if login:
#     st.session_state.runpage = user_login(authenticator=authenticator)
#
# if register:
#     st.session_state.runpage = user_registration(authenticator=authenticator)








