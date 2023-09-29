# Import required libraries and models
import uvicorn
from fastapi import FastAPI
from api.basemodels import GeneratePosts, GenerateEmail
from post_generator.main import generate
from email_generator.email_generator import EmailGenerator
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

# Create app object
app = FastAPI()

origins = ["http://localhost:3000"]  # Replace with your React app's URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Root endpoint
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# Endpoint to generate social media posts
# Accepts a request body that matches the GeneratePosts model
@app.post('/socialmedia')
def gen_posts(data:GeneratePosts):
    data = data.dict()
    brand = data['brand']
    description = data['description']
    work = data['work']
    posts_language = data['posts_language']
    topics_ideas_prompt_expansion = data['topics_ideas_prompt_expansion']
    platforms = data['platforms']
    generated_post = generate.generate_post(brand,description,work,posts_language,
                                        topics_ideas_prompt_expansion,platforms)
    return generated_post

# Endpoint to generate emails
@app.post('/emailgenerator')
def gen_email(data:GenerateEmail):
    data = data.dict()
    sender = data['sender']
    recipient = data['recipient']
    style = data['style']
    email_contents = data['email_contents']
    generated_email = EmailGenerator.gen_mail_format(sender,recipient,style,email_contents)
    return generated_email


handler = Mangum(app=app)

# Main function
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)