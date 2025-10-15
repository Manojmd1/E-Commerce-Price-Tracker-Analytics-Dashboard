import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import time
import urllib.parse

# --- MySQL connection ---
user = "manoj"
password = urllib.parse.quote_plus("manoj@123") 
host = "localhost"
database = "book_scraper_db"

# Correct connection string with default port
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# --- Scraper settings ---
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
books = []

for page in range(1, 11):
    url = BASE_URL.format(page)
    print(f"Scraping page {page}: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page {page}: {e}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select("article.product_pod")

    for item in items:
        title = item.h3.a["title"]
        price_raw = item.select_one("p.price_color").text.strip().replace("£", "")
        # Clean price and convert to float safely
        price = float(''.join(filter(lambda c: c.isdigit() or c == '.', price_raw)))
        rating = item.select_one("p.star-rating")["class"][1]
        availability = item.select_one("p.instock.availability").text.strip()

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        })

    time.sleep(1)  # Be polite to the server

# --- Save to MySQL ---
df = pd.DataFrame(books)

try:
    df.to_sql("books", con=engine, if_exists="append", index=False)
    print(f"Scraped {len(df)} books successfully and saved to MySQL!")
except Exception as e:
    print(f"Failed to save data to MySQL: {e}")
