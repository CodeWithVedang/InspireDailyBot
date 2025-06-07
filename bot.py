import tweepy
import requests

# Twitter API credentials (replace with your own)
API_KEY = "YOUR_API_KEY"
API_SECRET_KEY = "YOUR_API_SECRET_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=10)
        response.raise_for_status()
        data = response.json()[0]
        quote = f'"{data["q"]}" - {data["a"]}'
        return quote
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return "Stay inspired! #InspireDaily"

def main():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    quote_text = get_quote()
    print("Tweeting:", quote_text)
    api.update_status(status=quote_text)

if __name__ == "__main__":
    main()
