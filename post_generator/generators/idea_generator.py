# Import necessary modules and classes
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from post_generator.prompts import Prompts
from LLM_model.llm import LLM, GenerationItemType

# Define a class named IdeaGenerator
class IdeaGenerator:
    def __init__(self, brand: str, number_of_ideas: str, prompt_expansion: str):
        # Initialize the IdeaGenerator object with the provided parameters
        self.brand = brand  # Company brand name
        self.number_of_ideas = number_of_ideas  # Number of ideas to generate
        self.prompt_expansion = prompt_expansion  # Additional information for the prompt

    # Method to generate a list of social media post ideas
    def generate_ideas(self, topic):
        # Construct the prompt for generating social media post ideas
        prompt = f"Create a list of {self.number_of_ideas} social media post ideas (concise and specific) for their account about the topic '{topic}' in the format '- ...\n- ...' {Prompts.get_avoids()}"
        
        # Check if prompt_expansion is provided and append it to the prompt if not empty
        if (self.prompt_expansion != ""):
            prompt = prompt + f"\n\nTake this also into account: {self.prompt_expansion}"
        
        # Generate the ideas using the Language Model (LLM)
        ideas = [
            i.replace("- ", "")
            for i in LLM.generate(
                [HumanMessage(
                    content=prompt)], GenerationItemType.IDEAS
                )
            .content.strip()
            .split("\n")
            if len(i) > 2
        ][: self.number_of_ideas]
        
        # Return the generated ideas
        return ideas
