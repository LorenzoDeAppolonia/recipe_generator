import streamlit as st


ingredients_list = [word.strip() for word in st.session_state['recipe_to_modify']['ingredients'].split(',')]

options = st.multiselect(
    'Select the ingredients you want to keep',
    ingredients_list)