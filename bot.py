import tweepy
import requests

# Twitter API credentials (replace with your own)
API_KEY = "YOUR_API_KEY"
API_SECRET_KEY = "YOUR_API_SECRET_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"
def verify_tokens(api_key, api_secret_key, access_token, access_token_secret):
    tokens = {
        "API Key": api_key,
        "API Secret Key": api_secret_key,
        "Access Token": access_token,
        "Access Token Secret": access_token_secret,
    }

    for name, token in tokens.items():
        if not token or token.strip() == "":
            print(f"Error: {name} is empty!")
            return False
        if " " in token:
            print(f"Warning: {name} contains spaces (check if copied correctly).")
        if len(token) < 20:
            print(f"Warning: {name} looks unusually short (check if copied fully).")
    print("All tokens look OK format-wise.")
    return True


# Example: replace with your actual tokens to test
API_KEY = "xSoenJLJTrpKFZ0hgDVw0Rtl3"
API_SECRET_KEY = "2aTgkcl0G1aCGtuDIaRjgcHMtVnfczlIDvmYMXIblLm700qm7X"
ACCESS_TOKEN = "1552971906487586816-ctU0ZEllw7rqmkQrETK5yy7XkfcBWn"
ACCESS_TOKEN_SECRET = "jN4arqE1dFU9pKh85z4JKE03pPMo9BK5deyDjappmW74h"

if verify_tokens(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    print("Tokens are good. You can run your bot now.")
else:
    print("Fix token issues above before running the bot.")

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
