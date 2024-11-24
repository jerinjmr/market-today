# Market Today: AI-powered Stock Market Insights

A real-time stock news and recommendations platform powered by web scraping and AI insights. The system uses Flask for the backend, web scraping for data collection, and integrates with the Llama AI model for market insights.
Visit [MarketToday](https://jerinjmr.pythonanywhere.com/) to view free hosted website.

## Features

- 🔄 Real-time stock market news from multiple sources
- 🤖 AI-powered market insights using Llama 3.2
- 📊 Cached recommendations for better performance
- 🌐 Responsive web interface

## Technical Details

- **Backend**: Flask 3.0.2
- **Web Scraping**: BeautifulSoup4 4.12.3
- **AI Model**: Llama 3.2 via OpenRouter API
- **Deployment**: Docker with Gunicorn server
- **Caching**: Built-in LRU cache for performance

## Performance Features

- Request caching to minimize API calls
- Parallel URL fetching for faster data collection
- Streaming AI responses for better user experience
- Production-grade Gunicorn server with worker management

## Data & API Sources

- [MoneyControl](https://www.moneycontrol.com/)
- [Economic Times](https://economictimes.indiatimes.com/)
- [OpenRouter AI API](https://openrouter.ai/)

## Prerequisites

- Python 3.11 or higher
- [OpenRouter API Key](https://openrouter.ai/). Create a `.env` file as shown below:
    ```
    OPENROUTER_API_KEY=your_openrouter_api_key_here
    ```
- Docker Engine v26.1.4 or higher (optional)


## Installation

1. Clone the repository:
```bash
git clone https://github.com/jerinjmr/market-today.git
cd market-today
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Run server locally
```bash
python3 wsgi.py
```  
Go to http://localhost:5000/ to view the results in webpage.

### 2. Run server using Docker
```bash
docker build -t markettoday .
docker run -e OPENROUTER_API_KEY=your_api_key_here -p 5000:5000 markettoday

```
Go to http://localhost:5000/ to view the results in webpage.


## Disclaimer

This application is for educational purposes only. We are not SEBI registered financial advisors. Please conduct your own research before making any investment decisions.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [OpenRouter API Documentation](https://openrouter.ai/docs)
- [OpenAI API](https://platform.openai.com/docs/api-reference/chat/create)