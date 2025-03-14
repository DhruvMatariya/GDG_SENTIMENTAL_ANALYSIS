import praw
import configparser
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import threading
import time
from collections import deque
nltk.download('stopwords')
nltk.download('punkt_tab')
# Read config values
config = configparser.ConfigParser()
config.read('config.ini')

reddit_client_id = config['reddit']['client_id']
reddit_client_secret = config['reddit']['client_secret']
reddit_username = config['reddit']['username']
reddit_password = config['reddit']['password']
reddit_user_agent = config['reddit']['user_agent']

# Authenticate with the Reddit API
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    username=reddit_username,
    password=reddit_password,
    user_agent=reddit_user_agent
)

# Load the trained model and tokenizer
try:
    model = load_model('sentiment_model.h5')
    print("Model loaded successfully.")
except OSError:
    print("Error: sentiment_model.h5 not found. Make sure to train the model first.")
    exit()

# Load tokenizer (you need to save and load the tokenizer separately)
import pickle
try:
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    print("Tokenizer loaded successfully.")
except FileNotFoundError:
    print("Error: tokenizer.pickle not found. Make sure the tokenizer is saved during training.")
    exit()

# Define max_len (must be the same as used during training)
max_len = 200 #Or the value you used during training.

def clean_text(text):
    text = re.sub(r'http\S+|www\S+|@\S+', '', text)  # Remove URLs, mentions
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuation and numbers
    text = text.lower()  # Lowercase
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_tokens = [w for w in tokens if not w in stop_words]
    return " ".join(filtered_tokens)

def analyze_sentiment(text, model, tokenizer, max_len):
    """Analyzes the sentiment of a single text using the trained LSTM model."""
    cleaned_text = clean_text(text)
    filtered_text = remove_stopwords(cleaned_text)
    sequence = tokenizer.texts_to_sequences([filtered_text])
    padded_sequence = pad_sequences(sequence, maxlen=max_len, padding='post', truncating='post')
    prediction = model.predict(padded_sequence)[0][0]  # Get the probability
    sentiment = "Toxic" if prediction > 0.5 else "Non-toxic" #Classify based on 0.5 threshold.
    return sentiment, prediction

# Global data store (thread-safe)
reddit_data = deque(maxlen=20) # Store last 20 posts

def fetch_reddit_data(subreddit_name, num_posts=20):
    """Fetches Reddit posts from a subreddit, analyzes their sentiment, and stores the results."""
    try:
        subreddit = reddit.subreddit(subreddit_name)
        posts = subreddit.hot(limit=num_posts) #Fetch from "hot"

        for post in posts:
            text = post.title + "\n" + post.selftext  # Combine title and body
            print(f"Received Reddit post: {post.title}")

            sentiment, probability = analyze_sentiment(text, model, tokenizer, max_len)
            print(f"  Sentiment: {sentiment} (Probability: {probability:.4f})")

            reddit_data.appendleft({"title": post.title, "text": text, "sentiment": sentiment, "probability": probability})

    except Exception as e:
        print(f"Error fetching Reddit data: {e}")

if __name__ == "__main__":
    # Fetch Reddit data in a separate thread
    subreddit_name = "MachineLearning"  # Replace with the subreddit you want to analyze
    fetch_thread = threading.Thread(target=fetch_reddit_data, args=(subreddit_name,))
    fetch_thread.daemon = True
    fetch_thread.start()

    # Keep the main thread alive (optional, for demonstration)
    try:
        while True:
            time.sleep(5)
            #print(f"Currently storing {len(reddit_data)} reddit posts.")
    except KeyboardInterrupt:
        print("Exiting main thread.")