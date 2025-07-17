import requests
import os
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv
from datetime import datetime
import json

# Load environment variables from .env
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# Categorize articles based on keywords
def categorize_article(title, snippet):
    keywords = {
        "construction": ["construction", "infrastructure", "highway", "road", "building", "bridge"],
        "manufacturing": ["factory", "manufacturing", "production", "plant", "assembly"],
        "energy": ["gas", "power", "turbine", "energy", "electric", "transmission"],
        "agro-industry": ["agro", "cassava", "agriculture", "sapz", "processing zone"],
        "finance/investment": ["loan", "investment", "afdb", "fund", "export"],
        "defense/tech": ["military", "ai", "automation", "cng", "biochar", "defence"]
    }

    text = (title + " " + snippet).lower()
    for category, words in keywords.items():
        if any(word in text for word in words):
            return category
    return "other"

# Fetch news articles from SerpAPI
def fetch_news():
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_news",
        "q": "factory OR construction OR industrial OR compressor OR tender Nigeria",
        "hl": "en",
        "gl": "ng",
        "api_key": SERPAPI_KEY
    }
    response = requests.get(url, params=params)
    return response.json().get("news_results", [])

# Process raw articles
def process_articles(articles):
    processed = []
    for article in articles:
        title = article.get("title", "")
        snippet = article.get("snippet", "")
        url = article.get("link", "")
        date = article.get("date", "")
        category = categorize_article(title, snippet)

        summary_line = snippet.strip()[:300]
        suggestion_line = "No AI suggestion (feature disabled)."

        processed.append({
            "title": title,
            "url": url,
            "summary": summary_line,
            "suggestion": suggestion_line,
            "category": category,  # Already lowercase from categorize_article
            "date": date
        })
    return processed

# Group articles by category
def group_by_category(processed_articles):
    grouped = {}
    for article in processed_articles:
        cat = article["category"]
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(article)
    return grouped

# Generate HTML report using Jinja2
def generate_report(grouped_articles):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')
    return template.render(
        current_year=datetime.now().year,
        grouped_articles=grouped_articles
    )

# Main pipeline
def main():
    print("Fetching news...")
    articles = fetch_news()
    print(f"Found {len(articles)} articles.")

    print("Processing articles...")
    processed = process_articles(articles)

    # Save as JSON for JS frontend
    with open("static/articles.json", "w", encoding="utf-8") as f:
        json.dump(processed, f, ensure_ascii=False)

    grouped = group_by_category(processed)
    html = generate_report(grouped)

    # Save HTML report
    with open("nigeria.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ Report saved as nigeria.html — open it in your browser.")
    print("🗂 JSON saved as static/articles.json")

if __name__ == "__main__":
    main()
