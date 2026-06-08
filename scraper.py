import requests
from bs4 import BeautifulSoup
from database import save_quote

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        count = 0
        for q in quotes:
            text = q.find('span', class_='text').get_text()
            author = q.find('small', class_='author').get_text()
            tags = ', '.join([t.get_text() for t in q.find_all('a', class_='tag')])
            save_quote(text, author, tags)
            count += 1
        print(f"Scraped {count} quotes successfully!")
        return count
    except Exception as e:
        print(f"Scraping error: {e}")
        return 0
