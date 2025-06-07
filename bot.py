import tweepy
import requests
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

# Load credentials from environment
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# Authenticate
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Fetch quote from ZenQuotes API
response = requests.get("https://zenquotes.io/api/random")
data = response.json()[0]
quote = f"{data['q']} – {data['a']}"

# Create image with quote
img = Image.new('RGB', (800, 450), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("arial.ttf", 24)
except:
    font = ImageFont.load_default()

margin, offset = 40, 50
for line in quote.split('\n'):
    draw.text((margin, offset), line, font=font, fill=(0, 0, 0))
    offset += 30

img.save("quote.jpg")

# Post tweet with image
media = api.media_upload("quote.jpg")
api.update_status(status="#InspireDaily #QuoteOfTheDay", media_ids=[media.media_id])

print("✅ Tweet posted!")
