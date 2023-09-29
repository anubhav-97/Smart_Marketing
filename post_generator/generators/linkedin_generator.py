# Importing necessary modules and classes
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from post_generator.prompts import Prompts
from LLM_model.llm import LLM, GenerationItemType

# Define a class named LinkedInGenerator
class LinkedInGenerator:
    def __init__(self, brand: str, language: str, idea: str, prompt_expansion: str, work: str, description: str):
        # Initialize the LinkedInGenerator object with the provided parameters
        self.brand = brand  # Company brand name
        self.language = language  # Language for the post
        self.idea = idea  # The main idea or topic of the post
        self.prompt_expansion = prompt_expansion  # Additional information for the post
        self.description = description  # Description for the post
        self.work = work  # Type of work the company does

    # Method to generate a LinkedIn post
    def generate_post(self):
        # Construct the prompt for generating the LinkedIn post
        prompt = f"Write a LinkedIn post for the company named {self.brand} which is a {self.work} in {self.language} with 1-2 paragraphs for their account that talks about '{self.idea}' also give emphasis on this {self.description} {Prompts.get_avoids()}"
        
        # Check if prompt_expansion is provided and append it to the prompt if not empty
        if (self.prompt_expansion != ""):
            prompt = prompt + f"\n\nTake this also into account: {self.prompt_expansion}"
        
        # Generate the post using the Language Model (LLM)
        post = LLM.generate([HumanMessage(content=prompt)], GenerationItemType.POST).content.strip()
        
        return post
