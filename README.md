# Smart Marketer
### Introducing GPT Marketing Navigator: Revolutionizing Marketing Campaign.

The goal of Smart Marketer is to research how much can GPT-4 or LLM's be utilized to generate personalised email, Engaging social media posts and reduce a lot of manual work which inturn can save time and resources. Currently it uses GPT-3 to provide responses.

This uses langchain's HumanChatMessage package Which is like a A chat message representing information coming from a human interacting with the AI system.

## About Smart Marketer:

1. Social Media Campaign:

Firstly it creates topics on the instructions given by the person.\
Then it creates ideas according to the topics it has already generated\
Then finally it writes a very engaging post.\
It can also post the generated content on a company's page(currently it is only integrated with Twitter API)

It Offers suggestions according to the provided Brand name, Industry and brand description\
It Internally Generates a list of topics and formulates ideas for each one\
Currently, Facilitates post creation for Twitter,Facebook,Instagram, and LinkedIn\
Creates optimized post bodies automatically\
Selects hashtags intelligently so that the post get a good out reach\
It Allows you to write posts in any language\


2. Email Marketing Campaign:
It can Generate personalized email content using ChatGPT.\
It generates Idea according to the given instructions or if any particular topic is to be addressed and it write the each paragraph of the in a very precise way so that the message is conveyed in a very simplistic manner.\
It can draft subject lines, email body text, and call-to-action (CTA) messages tailored to individual recipient with context\
It can generate product recommendations, discount offer's or can Educate about the a particular product.\
It can adjust the tone/style accordingly weather the email style should be Forma, Casual or Neutral.\

# Tools and Technologies Used

**Frontend:** React, JavaScript, Node.js, HTML, CSS\
**Backend:** Python 3, Langchain, OpenAI API, FastAPI(To Build API)\
**Cloud Technologies:** AWS Lambda, AWS API Gateway, AWS S3\
**CI-CD pipeline:** Github Actions <br />

# How to start using Smart Marketer?
## Setup:
1. Firstly you should have python3 installed in you computer
2. run `git clone https://github.com/anubhav-97/Smart_Marketing.git` (clone the repo)
2. then run `pip install -r requirements.txt` (install all dependencies)
3. Please Enter an OpenAI API key in the LLM_model/llm.py file at the place of YOUR_API_KEY

## Backend Server:
1. Run `uvicorn api.app:app --reload` (this will run the backend server)

## Frontend Build:
1. Navigate to folder smartmarketing_app `cd React/smartmarketing_app`
2. Run `npm start` 

And you will be on the app...

## Deployment Steps:
1. Set up an AWS account and create an S3 bucket for storing your application code.

2. Obtain AWS credentials with appropriate permissions and store them as GitHub secrets:\
AWS_SECRET_ACCESS_KEY_ID\
AWS_SECRET_ACCESS_KEY\
AWS_DEFAULT_REGION\

3. GitHub Repository Setup:\
Make sure your FastAPI application code is hosted in a GitHub repository.

4. GitHub Secrets:

Go to your GitHub repository settings.\
Navigate to "Secrets" or "Settings" > "Secrets."\
Add the AWS credentials mentioned above as repository secrets.\
GitHub Actions Workflow:

5. Ensure that you have the .github/workflows/main.yml file in your repository with the workflow configuration 

6. Commit and Push:

Make changes to your FastAPI application code as needed.\
Commit and push the changes to the main branch of your GitHub repository.\

7. Continuous Integration (CI):
GitHub Actions will automatically trigger the CI workflow when you push changes to the main branch.

8. The CI workflow will:
Set up a Python environment.\
Create or use an existing Python virtual environment and install dependencies from requirements.txt.\
Create a zip archive of your application's dependencies.\
Upload the zip file as an artifact.\

9. Continuous Deployment (CD):
After the CI workflow completes successfully, the CD workflow will run if the conditions are met (main branch push event).\

10. The CD workflow will:
Install the AWS CLI and configure it with the provided credentials.\
Download the previously created zip archive from the CI artifacts.\
Upload the zip archive to an S3 bucket.\
Deploy the new Lambda function code with the uploaded zip file.\

11. Monitor Deployment:
Monitor the CD workflow's execution for any errors or issues.\
You can also check AWS Lambda for the updated function code.\

12. Access the FastAPI Application:
After successful deployment, your FastAPI application will be updated and accessible via AWS Lambda.
Repeat for Future Deployments:

Please feel free to present thoughts on this project at anubhav25sh@gmail.com

### In the near Future...
It can Generates AI Images for each post using Stable Diffusion, Dalle2 or Midjourney\
We can Connect it with the email smtp and extract all past emails and it will create personalised email based on the past conversation.\
It can analyze the email list and segment subscribers based on various criteria, such as demographics, behavior, or engagement level.
It can analyze recipient data and recommend the best times to send emails based on individual preferences and past behavior to increase open and click-through rates.