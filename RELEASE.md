# MarketToday v0.3.0 Release Notes 📈

## Highlights
Upgraded AI model for significantly better insights, overhauled UI responsiveness across devices, and removed MoneyControl dependency due to hosting restrictions.

---

## New Features 🌟

### AI Model Upgrade
* Upgraded from Llama 3.2 to `gpt-oss-20b` for higher quality market insights
* Improved prompt engineering for more actionable and relevant analysis
* Increased max token output to 3000 for longer, more detailed responses

### Timezone Support
* Added `pytz` package for accurate timezone handling across the application

---

## UI Enhancements 🎨

### Responsive Layout Overhaul
* Added comprehensive responsive breakpoints for mobile, tablet, and desktop
* Implemented flexbox-based layout for better content organization
* Optimized container widths and spacing across all screen sizes

### AI Insights Section
* Increased AI insights section prominence with 80vh height
* Improved visibility and accessibility of AI-generated content

### Footer & Layout Fixes
* Fixed footer positioning and overlap issues
* Ensured proper content flow without element collisions

---

## Technical Improvements 🔧

### MoneyControl Scraping Removal
* Removed MoneyControl page scraping entirely — blocked by Render's infrastructure (403 Forbidden)
* Removed date-based news sorting as the date field was unavailable from scrape responses
* This is a permanent removal, not a temporary workaround

### Documentation
* Updated README.md with correct model information

---

## Breaking Changes ⚠️
* MoneyControl is no longer a data source — news from MoneyControl will not appear in the application

## Data & API Sources
- [Economic Times](https://economictimes.indiatimes.com/)
- [OpenRouter AI API](https://openrouter.ai/)

## Browser Compatibility
* Chrome (latest)
* Firefox (latest)
* Safari (latest)
* Edge (latest)

## Installation Instructions
1. Clone the repository
2. Install required dependencies:
```bash
   pip install -r requirements.txt
```
3. Set up environment variables in `.env`
4. Run the application:
```bash
   python wsgi.py
```

## Contributors
- @jerinjmr & @jerin-scalers-ai
- @angeleenajohn

## Known Issues 🐛
* MoneyControl data source permanently removed due to Render hosting restrictions

---

# MarketToday v0.2.0 Release Notes 📈

## New Features 🌟

### Introduced AI Insights to Stock News
* AI-powered market insights to stock news using Llama 3.2 model

## UI Enhancements 🎨

### Modern Design Update
* New card-based layout with subtle shadows
* Improved typography using Segoe UI font family
* Added responsive container with max-width 1200px
* Enhanced color scheme with better contrast

### Interactive Elements
* Hover effects on table rows
* Smooth transitions for clickable elements
* Better visual hierarchy for content sections

### Loading States
* Added animated loading spinner
* Improved loading indicator with animated dots
* Smoother transition between loading and content states
* Added streaming response for better user experience
* Character-by-character text animation for smoother content display

## Technical Improvements 🔧
* Added streaming endpoint for AI content delivery
* Implemented error handling for API requests
* Added response timeout handling
* Improved content caching mechanism

## Performance Optimizations ⚡
* Delayed AI content loading for faster initial page load
* Optimized streaming response handling
* Improved CSS animations performance

## Data & API Sources
- [MoneyControl](https://www.moneycontrol.com/)
- [Economic Times](https://economictimes.indiatimes.com/)
- [OpenRouter AI API](https://openrouter.ai/)

## Browser Compatibility
* Chrome (latest)
* Firefox (latest)
* Safari (latest)
* Edge (latest)

## Installation Instructions
1. Clone the repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env`
4. Run the application:
   ```bash
   python wsgi.py
   ```

## Contributors
- @jerinjmr & @jerin-scalers-ai 
- @angeleenajohn 


## Known Issues 🐛
* None reported in this release


#  MarketToday v0.1.0 Release Notes 📈
## Features
- Stock market news and recommendation using web scraping
- Data source: Moneycontrol & Economic Times
- Python flask based server for web hosting
- Support for hosting app in Heroku

---
*For any issues or feedback, please create an issue in the repository.*
