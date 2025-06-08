# generate_page.py
import requests
from datetime import datetime

def fetch_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random")
        res.raise_for_status()
        data = res.json()
        return data[0]["q"], data[0]["a"]
    except Exception as e:
        return "Stay positive, work hard, make it happen.", "Unknown"

def generate_html(quote, author):
    now = datetime.now().strftime("%B %d, %Y %I:%M %p")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Quote</title>
    <style>
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to right, #e0eafc, #cfdef3);
            text-align: center;
            padding: 20px;
        }}
        .container {{
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            max-width: 600px;
        }}
        blockquote {{
            font-size: 1.5rem;
            font-style: italic;
            color: #333;
        }}
        footer {{
            margin-top: 1rem;
            font-size: 1.1rem;
            color: #555;
        }}
        .timestamp {{
            margin-top: 2rem;
            font-size: 0.9rem;
            color: #888;
        }}
    </style>
</head>
<body>
    <div class="container">
        <blockquote>“{quote}”</blockquote>
        <footer>- {author}</footer>
        <div class="timestamp">Last updated on {now}</div>
    </div>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    quote, author = fetch_quote()
    generate_html(quote, author)
