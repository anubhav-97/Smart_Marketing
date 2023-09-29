# Import necessary modules and classes
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from post_generator.prompts import Prompts
from LLM_model.llm import LLM, GenerationItemType

# Define a class named TweetGenerator
class TweetGenerator:
    def __init__(self, brand: str, language: str, idea: str, prompt_expansion: str, work: str, description: str):
        # Initialize the TweetGenerator object with the provided parameters
        self.brand = brand  # Company brand name
        self.language = language  # Language for the tweet
        self.idea = idea  # The main idea or topic of the tweet
        self.prompt_expansion = prompt_expansion  # Additional information for the tweet
        self.work = work  # Type of work the company does
        self.description = description  # Description for the tweet

    # Method to generate a Tweet
    def generate_tweet(self):
        # Construct the prompt for generating the tweet
        prompt = f"Write a Tweet in {self.language} for a brand named {self.brand} which is {self.work} for their account that talks about {self.idea} its description about this company is {self.description} {Prompts.get_avoids()}"
        
        # Check if prompt_expansion is provided and append it to the prompt if not empty
        if (self.prompt_expansion != ""):
            prompt = prompt + f"\nTake this also into account: {self.prompt_expansion}"
        
        # Generate the tweet using the Language Model (LLM)
        tweet = LLM.generate(
            [HumanMessage(
                content=prompt)], GenerationItemType.POST
        ).content.strip()
        
        return tweet
