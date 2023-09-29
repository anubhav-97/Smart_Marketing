# Import necessary modules and classes
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from post_generator.prompts import Prompts
from LLM_model.llm import LLM, GenerationItemType

# Define a class named FacebookGenerator
class FacebookGenerator:
    def __init__(self, brand: str, language: str, idea: str, prompt_expansion: str, work: str, description: str):
        # Initialize the FacebookGenerator object with the provided parameters
        self.brand = brand
        self.language = language
        self.idea = idea
        self.prompt_expansion = prompt_expansion
        self.work = work
        self.description = description
    # Method to generate a Facebook post
    def generate_post(self):
        # Construct the prompt for generating the Facebook post
        prompt = f"Write a facebook post for the company named{self.brand} which is a {self.work} in {self.language} for their account that talks about '{self.idea}' also give emphasis on this{self.description} {Prompts.get_avoids()}"
        # Check if prompt_expansion is provided and append it to the prompt if not empty
        if (self.prompt_expansion != ""):
            prompt = prompt + \
                f"\n\nTake this also into account: {self.prompt_expansion}"

        # Generate the post using the Language Model (LLM)
        post = LLM.generate(
            [HumanMessage(
                content=prompt)], GenerationItemType.POST
        ).content.strip()

        return post
