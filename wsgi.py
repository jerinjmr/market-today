"""Stock recommendation system.

Uses python flask to start web server.
"""
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, Response, stream_with_context
from scrape import get_stock_reco
from openai import OpenAI
from functools import lru_cache
import pytz

app = Flask(__name__)
# Load environment variables from .env file
load_dotenv()

# Cache stock recommendations for 5 minutes
@lru_cache(maxsize=1)
def cached_stock_reco():
    timestamp = int(time.time() / 300)  # Cache invalidates every 5 minutes
    return get_stock_reco(), timestamp

@app.route("/")
def calls():
    """Render the index page."""
    market_feed, _ = cached_stock_reco()
    headlines = "\n".join([news[1] for news in market_feed])
    return render_template(
        "index.html", 
        calls=market_feed, 
        ai_content="Loading...",
        headlines=headlines
    )

@app.route("/get-ai-insight")
def stream_ai_insight():
    """Stream AI-generated insights."""
    def generate():
        try:
            market_feed, _ = cached_stock_reco()
            headlines = "\n".join([news[1] for news in market_feed])
            india_tz = pytz.timezone("Asia/Kolkata")
            date = datetime.now(india_tz).date()

            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENROUTER_API_KEY"),
                timeout=30.0  # Add timeout
            )

            stream = client.chat.completions.create(
                model="openai/gpt-oss-20b:free",
                max_tokens=3000,
                stream=True,
                messages=[
                    {
                        "role": "system",
                        "content": f"Generate short, crisp and clear summary of stock market news for the day {date}. \
                            Clearly list down buy and sell recommendations. \
                            Title should be just Stock Market Today and the entire response \
                            should be in 2800 words maximum.",
                    },
                    {"role": "user", "content": headlines},
                ]
            )

            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Error generating insights: {str(e)}"

    return Response(
        stream_with_context(generate()), 
        mimetype='text/event-stream',
        headers={'Cache-Control': 'no-cache'}
    )

if __name__ == "__main__":
    app.run()
