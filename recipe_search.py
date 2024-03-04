import streamlit as st
from st_pages import add_page_title
from recipe_llm import final_chain
from db.recipes_db import recipes as recipes_collection

user_recipes = []
add_page_title()

minuti = st.slider(label= 'Preparation time :clock1:', min_value= 5, max_value=60)
cosine_type = st.selectbox('What cuisine do you want to cook?', ('Italian', 'Chinese', 'Vegetarian', 'French', 'Indian', 'Japanese', 'Thai'))
ingredients = st.chat_input(placeholder='Inserisci ingredienti')
if ingredients:
    with st.spinner('Looking for the recipe that suits you...'):
        recipe = final_chain({'ingredients': ingredients, 'cuisine':cosine_type, 'minuti': minuti})
    st.write(f"RECIPE: {recipe['recipe_name']}\n\nINGREDIENTS: {recipe['ingredients']}\n\nSTEPS: {recipe['recipe_instructions']}\n\n")
    st.session_state['ingredients'] = True
    st.session_state['recipe'] = recipe

add_checkbox = st.checkbox('Add to my cookbook')
if add_checkbox and st.session_state['ingredients']:
    recipe = st.session_state['recipe']
    recipes_collection.insert_one({'recipe_name': recipe['recipe_name'], 'ingredients': recipe['ingredients'], 'recipe_instructions': recipe['recipe_instructions'], 'minuti': recipe['minuti']})
    st.write("Recipe added to your cookbook! :smile:")
    st.toast('Recipe added to your cookbook!', icon='🎉')
    st.session_state['ingredients'] = False
    st.session_state['recipe'] = None





