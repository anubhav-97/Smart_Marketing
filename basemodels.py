from pydantic import BaseModel
# Define a Pydantic BaseModel for describing the generation of posts
class GeneratePosts(BaseModel):
    brand: str
    description: str
    work:str 
    posts_language:str
    topics_ideas_prompt_expansion:str
    platforms:str

# Define another Pydantic BaseModel for generating emails
class GenerateEmail(BaseModel):
    sender:str
    recipient:str
    style:str
    email_contents: list