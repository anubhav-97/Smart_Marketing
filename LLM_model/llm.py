# Import necessary modules and classes
from langchain.chat_models import ChatOpenAI
from enum import Enum
import os

# Import the OpenAI API key (assuming it's provided)
# Load the API key from the .env file
os.environ["OPENAI_API_KEY"] = "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"


# Define an enumeration for different generation item types
class GenerationItemType(Enum):
    TOPICS = 1
    IDEAS = 2
    POST = 3

# Define a class named LLM (Language Model)
class LLM:
    # Initialize the GPT-3.5 Turbo model with specific parameters
    gpt3 = ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo")

    # Static method to generate content based on the given prompt and item type
    @staticmethod
    def generate(prompt: str, type: GenerationItemType):
        # Generate content based on the specified item type
        if type == GenerationItemType.TOPICS:
            return LLM.gpt3(prompt)

        if type == GenerationItemType.IDEAS:
            return LLM.gpt3(prompt)

        if type == GenerationItemType.POST:
            return LLM.gpt3(prompt)
