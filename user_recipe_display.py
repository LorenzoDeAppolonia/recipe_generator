import streamlit as st
from st_pages import add_page_title
from db.recipes_db import recipes as recipes_collection


def get_user_recipes():
    return recipes_collection.find()


add_page_title()


for el in get_user_recipes():
    container = st.container()
    with container:
        st.header(el['recipe_name'])
        st.text(f"Ingredients: {el['ingredients']}")

        see_recipe = st.button(key=el['recipe_name'], label='See recipe')
        if see_recipe:
            st.write(
                f"STEPS: {el['recipe_instructions']}\n\nCOOKING TIME: {el['minuti']} min\n\n")

        modify_recipe = st.button(key=f"{el['recipe_name']}_modify", label='Modify recipe :hammer_and_pick:')
        if modify_recipe:
            pass
            # TO BE IMPLEMENTED

