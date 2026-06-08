import schedule
import time
import threading
from scraper import scrape_quotes

def run_scheduler():
    schedule.every(10).minutes.do(scrape_quotes)
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    thread = threading.Thread(target=run_scheduler, daemon=True)
    thread.start()
    print("Scheduler started - scraping every 10 minutes!")
