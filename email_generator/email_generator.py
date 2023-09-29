import os
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI
from LLM_model.llm import LLM, GenerationItemType

# Define a class for email generation
class EmailGenerator:
    # Define a method to generate email contents
    def gen_mail_contents(email_contents):

        # Iterate through all separate topics in the email_contents list
        for topic in range(len(email_contents)):
            # Get the input text for the current topic
            input_text = email_contents[topic]
            # Create a prompt for rewriting the text to be elaborate and polite
            prompt=f"Rewrite the text to be elaborate and polite.\nAbbreviations need to be replaced.\nText: {input_text}\nRewritten text:"
            # Generate a rephrased content using the Language Model (LLM)
            rephrased_content = LLM.generate([HumanMessage(content=prompt)], GenerationItemType.POST).content.strip()
            # Replace the existing topic text with the updated rephrased content
            email_contents[topic] = rephrased_content
        return email_contents

    # Define a method to generate the final email format
    def gen_mail_format(sender, recipient, style, email_contents):
        # Update the email contents with more formal statements
        email_contents = EmailGenerator.gen_mail_contents(email_contents)

        contents_str, contents_length = "", 0
        # Aggregate all contents into one string
        for topic in range(len(email_contents)):
            contents_str = contents_str + email_contents[topic]
            # Calculate the total characters in the email contents
            contents_length += len(email_contents[topic])
            # Create a prompt for generating a professional 2-3 paragraph email        
            prompt=f"Write a professional 2-3 paragraph email sounds {style}.\n\nSender: {sender}\nRecipient: {recipient} {contents_str}\n\nEmail Text:"
       
        # Generate the final email text using the Language Model (LLM)
        email_final_text = LLM.generate([HumanMessage(content=prompt)], GenerationItemType.POST).content.strip()

        return email_final_text