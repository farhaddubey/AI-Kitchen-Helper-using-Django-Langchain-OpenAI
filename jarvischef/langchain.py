import os

from dotenv import load_dotenv
from langchain_core.prompts import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain_openai import ChatOpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

def askJarvisChef(recipe_message):
    chat = ChatOpenAI(model="gpt-3.5-turbo-0125", openai_api_key=SECRET_KEY )

    systemMessagePrompt=SystemMessagePromptTemplate.from_template(
        """Your name is Knights. You are a master chef so first introduct yourself. You can only write of any type of food recipe which can 
        be cooked at five minute. You are only allowed to write food related queries. Well your romantic too. So you reply in a flirty manner."""
    )
    HumanMessagePrompt=HumanMessagePromptTemplate.from_template(
        '{asked_recipe}'
    )
    chatPrompt=ChatPromptTemplate.from_messages([
        systemMessagePrompt, HumanMessagePrompt
    ])
    formattedChatPrompt=chatPrompt.format_messages(
        asked_recipe=recipe_message
    )
    response=chat.invoke(formattedChatPrompt)
    print("Formatted Chat ", response)
    return response.content