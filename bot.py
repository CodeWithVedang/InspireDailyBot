import os
import tweepy
import requests

# Twitter API credentials from environment variables
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# Authenticate Twitter API
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def get_quote():
    # Example free quote API - returns JSON with quote and author
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = response.json()
    quote = data.get("content", "Be positive and keep going!")
    author = data.get("author", "Unknown")
    return f'"{quote}" — {author}'

def main():
    quote_text = get_quote()
    try:
        # Tweet the quote text
        api.update_status(status=quote_text)
        print("Quote tweeted successfully!")
    except Exception as e:
        print("Error posting tweet:", e)

if __name__ == "__main__":
    main()
