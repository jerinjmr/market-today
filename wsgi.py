"""Stock recommendation system.

Uses python flask to start web server.
"""
from flask import Flask, render_template
from scrape import get_stock_reco

app = Flask(__name__)


@ app.route("/")
def calls():
    """Render the index page."""
    market_feed = get_stock_reco()
    return render_template('index.html', calls=market_feed)


if __name__ == '__main__':
    app.run()
