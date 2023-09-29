# Import necessary modules and classes
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from post_generator.prompts import Prompts
from LLM_model.llm import LLM
from LLM_model.llm import LLM, GenerationItemType

# Define a class named TopicGenerator
class TopicGenerator:
    def __init__(self, brand: str, topic_count: str, prompt_expansion: str, work: str):
        # Initialize the TopicGenerator object with the provided parameters
        self.brand = brand  # Company brand name
        self.prompt_expansion = prompt_expansion  # Additional information for the prompt
        self.topic_count = topic_count  # Number of topics to generate
        self.work = work  # Type of work the company does

    # Method to generate a list of general topics or fields for social media posts
    def generate_topics(self):
        # Construct the prompt for generating topics
        prompt = f"Create a list of {self.topic_count} general topics or fields to cover in their social media posts for a company which works as a {self.work}, in the format '- ...\n- ...' {Prompts.get_avoids()}"
        
        # Check if prompt_expansion is provided and append it to the prompt if not empty
        if (self.prompt_expansion != ""):
            prompt = prompt + f"\n\nTake this also into account: {self.prompt_expansion}"
        
        # Generate the topics using the Language Model (LLM)
        topics = [
            i.replace("- ", "")
            for i in LLM.generate([HumanMessage(content=prompt)], GenerationItemType.IDEAS)
            .content.strip()
            .split("\n")
            if len(i) > 2
        ][: self.topic_count]
        
        # Log and format the generated topics
        # Logger.log(format_list(topics))
        
        # Return the generated topics
        return topics
