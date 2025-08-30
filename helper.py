import dotenv
import os
import getpass
from langchain.prompts import PromptTemplate
from langchain.chains.sequential import SequentialChain
from langchain.chains.llm import LLMChain
dotenv.load_dotenv()
if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass('GOOGLE_API_KEY') 

from langchain.chat_models import init_chat_model

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai", temperature=.6)


def generate_restaurant_name_and_item(cuisine):


    prompt_template_name=PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurent for {cuisine} Food. Suggest a fency name for this i want only name not preamble and no postamble i want only one name"
    )


    name_chain=LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")


    prompt_template_items=PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some Menu item for {restaurant_name}. Return as a commma seperated Value not Preamble and postamble"""
    )

    food_item_chain=LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_item")
    
    
    chains=SequentialChain(chains=[name_chain, food_item_chain],
                       input_variables=['cuisine'],
                       output_variables=['restaurant_name', 'menu_item'])


    response=chains({"cuisine":cuisine})
    return response


if __name__ =="__main__":
    print(generate_restaurant_name_and_item("Italian"))
