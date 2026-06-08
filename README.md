# automated-web-scraper
An automated web scraping tool built with Python and Flask that scrapes quotes periodically and stores them in a database with a live dashboard.

## 🚀 Features
- Automated web scraping using BeautifulSoup
- Scheduled scraping every 10 minutes
- SQLite database storage
- CSV export functionality
- Live Flask dashboard
- REST API for scraped data

## 🛠️ Technologies Used
- Python
- Flask
- BeautifulSoup4
- Requests
- Schedule
- SQLite
- HTML, CSS, JavaScript

## 📁 Project Structure
automated-web-scraper/
├── app.py          # Flask application
├── scraper.py      # Scraping logic
├── scheduler.py    # Auto-scheduler
├── database.py     # SQLite storage
├── templates/
│   └── index.html  # Dashboard UI
├── static/
│   └── style.css   # Styling
└── requirements.txt
## ⚙️ Installation & Setup
```bash
# Clone the repository
git clone https://github.com/nansipatibandla/automated-web-scraper.git
cd automated-web-scraper

# Install dependencies
pip install flask requests beautifulsoup4 schedule

# Run the application
python app.py
💻 Usage
Open browser and go to http://127.0.0.1:5000
Dashboard shows all scraped quotes
Click Scrape Now to scrape immediately
Click Export CSV to download data
Auto-scrapes every 10 minutes in background
📊 Data Collected
Quote text
Author name
Tags
Scraped timestamp
👩‍💻 Developer
Nancy Patibandla
GitHub: @nansipatibandla
