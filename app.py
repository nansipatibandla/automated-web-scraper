from flask import Flask, render_template, jsonify
from database import init_db, get_all_quotes, export_to_csv
from scraper import scrape_quotes
from scheduler import start_scheduler

app = Flask(__name__)
init_db()
scrape_quotes()
start_scheduler()

@app.route('/')
def index():
    quotes = get_all_quotes()
    return render_template('index.html', quotes=quotes, total=len(quotes))

@app.route('/scrape')
def scrape_now():
    count = scrape_quotes()
    return jsonify({'message': f'Scraped {count} quotes!', 'total': len(get_all_quotes())})

@app.route('/export')
def export():
    total = export_to_csv()
    return jsonify({'message': f'Exported {total} quotes to quotes.csv!'})

@app.route('/api/quotes')
def api_quotes():
    quotes = get_all_quotes()
    return jsonify([{'id': r[0], 'text': r[1], 'author': r[2], 'tags': r[3], 'scraped_at': r[4]} for r in quotes])

if __name__ == '__main__':
    app.run(debug=True)
