import os
from langchain.chains import SequentialChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

# API KEY:

os.environ['OPENAI_API_KEY'] = ''


# LLM:

llm = OpenAI(temperature=0)


# PROMPTING

prompt_recipe_name = PromptTemplate.from_template(
           'You are a culinary assistant, assisting housewives in researching and preparing recipes. Given the following list of ingredients:'
           'ingredients: '
           '"""'
           '{ingredients}'
           '""'
           'I want to cook a'
           'cuisine:'
           '"""'
           '{cuisine} '
           '"""'
           'dish that has a preparation time of no more than {minuti} minutes. Suggest a recipe that I could cook. Answer with just the name of the recipe.')

recipe_name_chain = LLMChain(llm=llm, prompt=prompt_recipe_name, output_key='recipe_name')

prompt_recipe_instructions = PromptTemplate.from_template(
           'Given this recipe:'
           '"""'
           'recipe: '
           '"""'
           '{recipe_name}'
           '"""'
           'tell me the list of steps required to cook it with just the following ingredients:'
           'ingredients:'
           '"""'
           '{ingredients} and pepper, salt, oil and vinegar.'
           '"""'
           'You are forbidden to include other ingredients, instead only use the ingredients listed above.')

recipe_instructions_chain = LLMChain(llm=llm, prompt=prompt_recipe_instructions, output_key='recipe_instructions')

final_chain = SequentialChain(
    chains = [recipe_name_chain, recipe_instructions_chain],
    output_variables = ['recipe_name','recipe_instructions'],
    input_variables = ['ingredients', 'cuisine', 'minuti']
)

