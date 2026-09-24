# Book Scraper

A Python script that scrapes book titles and prices from a bookstore site
and saves the results to a CSV file.

## Features
- **Web Scraping:** Uses `requests` to fetch pages and `BeautifulSoup` to parse HTML.
- **Error Handling:** Network failures are caught and reported instead of crashing the script.
- **CSV Export:** Saves results in a clean, spreadsheet-ready format.

## Tech Stack
- Python 3.8+
- `requests`, `beautifulsoup4`

## Project Structure
```text
book-scraper/
├── book_scraper.py    # Main scraper script
└── .gitignore
```

## Getting Started

### Prerequisites
Python 3.8 or higher

### Installation
```bash
pip install requests beautifulsoup4
```

### Usage
```bash
python book_scraper.py
```
This creates a `books.csv` file with the scraped titles and prices.
