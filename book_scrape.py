"""
Book Scraper
------------
Visits a bookstore website and collects the title and price of every
book listed on the page, then saves the results to a CSV file.

Site used: https://books.toscrape.com
(a public sandbox site made specifically for practicing web scraping)
"""

import csv
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com"


def fetch_page(url):
    """Download the raw HTML of a page. Returns None if it fails."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises an error for 404, 500, etc.
        return response.text
    except requests.RequestException as error:
        print(f"Could not reach {url}: {error}")
        return None


def parse_books(html):
    """Take raw HTML and pull out each book's title and price."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for article in soup.select("article.product_pod"):
        title_tag = article.h3.a
        price_tag = article.select_one("p.price_color")

        if not title_tag or not price_tag:
            # Skip anything that doesn't have both pieces we need
            continue

        title = title_tag["title"].strip()
        price = price_tag.text.strip()

        books.append({"title": title, "price": price})

    return books


def save_to_csv(books, filename="books.csv"):
    """Write the list of books to a CSV file."""
    if not books:
        print("No books to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price"])
        writer.writeheader()
        writer.writerows(books)

    print(f"Saved {len(books)} books to {filename}")


def main():
    html = fetch_page(URL)
    if html is None:
        return  # fetch_page already printed the error

    books = parse_books(html)
    save_to_csv(books)


if __name__ == "__main__":
    main()