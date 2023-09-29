# Import necessary modules and classes
import os
from LLM_model.llm import LLM
from post_generator.generators.topic_generator import TopicGenerator
from post_generator.generators.idea_generator import IdeaGenerator
from post_generator.generators.tweet_generator import TweetGenerator
from post_generator.generators.facebook_generator import FacebookGenerator
from post_generator.generators.instagram_generator import InstagramGenerator
from post_generator.generators.linkedin_generator import LinkedInGenerator
import tweepy

# Function to post a tweet
def post_to_twitter(tweet_content):
    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler("RZCKAGkXhbcMkIhNkYclfeZ", "OkDytvKSIsQEyvRgsSr7OaFCgxtvH8Doai0TYCm32Hxaz22H")
    auth.set_access_token("13927228432577027-CewPQELnvBrQPek91RWxxDLGhD04kw", "BpZMFH8xlL4BjNkCuzAwZcvFAjJNch2zbIfmhT7Jvwo")
    api = tweepy.API(auth, wait_on_rate_limit=True)
    api.update_status(status=tweet_content)


# Create a class for generating posts
class generate():
    
    def generate_post(brand,description, work, posts_language, topics_ideas_prompt_expansion, platforms):
        topic_count = int(1)
        ideas_per_topic = int(3)
        print('\n Nice! Started generating...\n')
        platforms = platforms.lower()

        # Generate topics based on provided information
        topics = TopicGenerator(brand, topic_count, topics_ideas_prompt_expansion, work).generate_topics()

        # Generate ideas for each topic
        for topic in topics:
            ideas = IdeaGenerator(brand, ideas_per_topic, topics_ideas_prompt_expansion).generate_ideas(topic)
            
            # Duplicate the list of ideas (not clear why it's duplicated)
            ideas=ideas+ideas
        
         # Iterate through the generated ideas
        for idea in ideas:
            if "twitter" in platforms:
                # Generate a tweet based on the idea
                gen_tweet = TweetGenerator(brand, posts_language, idea, topics_ideas_prompt_expansion, work, description).generate_tweet()
                return gen_tweet
                # Check if the tweet is shorter than 150 characters and post it to Twitter
                if len(tweet) <150:
                    post_to_twitter(gen_tweet)
                sys.exit()
            if "facebook" in platforms:
                # Generate a Facebook post based on the idea
                gen_fbpost =FacebookGenerator(brand, posts_language, idea, topics_ideas_prompt_expansion, work, description).generate_post()
                return gen_fbpost
            if "instagram" in platforms:
                # Generate an Instagram post based on the idea
                gen_instapost = InstagramGenerator(brand, posts_language, idea, topics_ideas_prompt_expansion, work, description).generate_post()
                return gen_instapost
            if "linkedin" in platforms:
                # Generate a LinkedIn post based on the idea
                gen_linkedinpost = LinkedInGenerator(brand, posts_language, idea, topics_ideas_prompt_expansion, work, description).generate_post()
                return gen_linkedinpost
            



