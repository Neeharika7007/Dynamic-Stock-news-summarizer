import requests
import os
from dotenv import load_dotenv

load_dotenv()  # This loads your API key from .env file

NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # Reads your NewsAPI key securely

def fetch_news(company):
    url = f"https://newsapi.org/v2/everything?q={company}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    return articles[:5]  # Returns latest 5 articles

