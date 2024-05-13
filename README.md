SENTIMENT ANALYSIS AND PERSONALIZED MESSAGING FOR CLINICAL TRIAL ON REDDIT

PROJECT SETUP INSTRUCTION:

•	Install Python from the official Python website if not already installed.
•	Install required libraries using pip: praw, nltk, and openai.
•	Download the VADER lexicon using nltk in a Python environment.
•	Obtain Reddit API credentials (client ID, client secret, user agent) and OpenAI API key from their respective platforms.
•	Update the subreddit_names list in the code with relevant subreddits as per your choice  related to clinical trials.

METHODOLOGY:

1.	Scraping Reddit Data:
•	Utilized the Python library PRAW (Python Reddit API Wrapper) to access Reddit's API.
•	Defined a function to scrape posts from specified subreddits related to clinical trials.
•	Extracted relevant information such as post titles, bodies, authors, and subreddit names for analysis.
2.	Sentiment Analysis:
•	Employed NLTK's VADER SentimentIntensityAnalyzer to perform sentiment analysis on the scraped post bodies.
•	Classified the sentiment of each post as positive, negative, or neutral based on sentiment scores.
•	Used sentiment analysis results to gauge user opinions and receptiveness towards clinical trials.
3.	Message Generation:
•	Leveraged OpenAI's API to generate personalized messages aimed at users based on their sentiment towards clinical trials.
•	Incorporated user-specific context from the posts to create engaging and relevant messages.
•	Messages were designed to encourage participation in clinical trials while respecting user sentiments.
