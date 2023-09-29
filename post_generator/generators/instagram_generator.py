# Import necessary modules and classes
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from post_generator.prompts import Prompts
from LLM_model.llm import LLM, GenerationItemType

# Define a class named InstagramGenerator
class InstagramGenerator:
    def __init__(self, brand: str, language: str, idea: str, prompt_expansion: str, work: str, description: str):
        # Initialize the InstagramGenerator object with the provided parameters
        self.brand = brand  # Company brand name
        self.language = language  # Language for the post
        self.idea = idea  # The main idea or topic of the post
        self.prompt_expansion = prompt_expansion  # Additional information for the post
        self.work = work  # Type of work the company does
        self.description = description  # Description for the post

    # Method to generate an Instagram post
    def generate_post(self):
        # Constructed the prompt for generating the Instagram post
        prompt = f"Write an Instagram post for the company named {self.brand} which is a {self.work} in {self.language} for their account that talks about '{self.idea}' also give emphasis on this {self.description} {Prompts.get_avoids()}"
        
        # Check if prompt_expansion is provided and append it to the prompt if not empty
        if (self.prompt_expansion != ""):
            prompt = prompt + f"\n\nTake this also into account: {self.prompt_expansion}"
        
        # Generate the post using the Language Model (LLM)
        post = LLM.generate(
            [HumanMessage(
                content=prompt)], GenerationItemType.POST
        ).content.strip()
       
        # Return the generated post
        return post
