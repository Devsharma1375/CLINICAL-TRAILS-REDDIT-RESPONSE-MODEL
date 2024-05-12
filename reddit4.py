import praw
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import openai
import csv

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Initialize Reddit API
reddit = praw.Reddit(client_id='********************',
                     client_secret='****************',
                     user_agent='*******************')
# Replace with your own reddit api crendidentials 

# Initialize NLTK's VADER SentimentIntensityAnalyzer
sia = SIA()

# Initialize OpenAI API
openai.api_key ='********************' # add your own open ai api key 

def scrape_reddit(subreddit_names, limit=10):
    data = []
    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)
        posts = subreddit.new(limit=limit)
        for post in posts:
            if post.selftext:  # Check if the post has a body (not empty)
                data.append({
                    'title': post.title,
                    'body': post.selftext,
                    'author': post.author.name,  # Include author's name for personalization
                    'subreddit': subreddit_name  # Include subreddit name
                })
    
    return data

def save_to_csv(data, filename='reddit_data.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'body', 'author', 'subreddit']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for post in data:
            writer.writerow(post)

def analyze_sentiment(text):
    pol_score = sia.polarity_scores(text)
    sentiment_scores = {
        'positive': pol_score['pos'],
        'negative': pol_score['neg'],
        'neutral': pol_score['neu']
    }
    max_sentiment = max(sentiment_scores, key=sentiment_scores.get)
    return max_sentiment

def generate_openai_message(sentiment, author_name, post_context):
    if sentiment == 'positive':
        prompt = f"User {author_name} is talking about {post_context}. Generate a positive message about clinical trials."
    elif sentiment == 'negative':
        prompt = f"User {author_name} is talking about {post_context}. Generate a negative message about clinical trials."
    else:
        prompt = f"User {author_name} is talking about {post_context}. Generate a neutral message about clinical trials."
    
    # Use OpenAI's API to generate a message based on the prompt
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response['choices'][0]['text'].strip()

def main():
    subreddit_names = ['psychology', 'mentalhealth', 'depression']  # Add more relevant subreddits here
    reddit_data = scrape_reddit(subreddit_names)
    save_to_csv(reddit_data)  # Save scraped data to CSV
    
    for post in reddit_data:
        post_body = post['body']
        post_context = post_body[:50]  # Extract first 50 characters as context
        post_body_sentiment = analyze_sentiment(post_body)
        author_name = post['author']
        
        openai_message = generate_openai_message(post_body_sentiment, author_name, post_context)
        print("Post Title:", post['title'])
        print("Sentiment:", post_body_sentiment)
        print("Subreddit:", post['subreddit'])
        print("OpenAI Message:", openai_message)
        print("\n")

if __name__ == "__main__":
    main()
