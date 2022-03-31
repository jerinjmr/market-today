# Web Scraping
Extracting large amount of data from websites.

## Web Scraping Libraries/Frameworks
### 1. Beautiful Soup
Popular Python package for web scraping. It is used to fetch data from html and xml files.  
`pip install beautifulsoup4`

### 2. Request
To make http requests  
`pip install requests`

### 3. Scrapy
Framework for web scrapping: https://scrapy.org/ 

## Run program locally
`python3 wsgi.py`
Go to 'http://127.0.0.1:5000/' to view the results in webpage.

## Host Website using Heroku

### 1. Prerequisite
* [Heroku Account](https://www.heroku.com/platform)
* [Heroku cli](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)  
Ubuntu installation: `sudo snap install heroku --classic`
* Git

### 2. Deploy Application using Heroku CLI
1. `heroku login`
2. `heroku create jmrinvestments`
3. `git push heroku` 

Finally, web app will be deployed on http://jmrinvestments.herokuapp.com. 

## References
* [Web Scraping](https://www.excellarate.com/blogs/web-scraping-introduction-applications-and-best-practices/#:~:text=Web%20scraping%20typically%20extracts%20large,show%20data%20from%20a%20website.)
* [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/ )
* [Python flask application deployment in Heroku - Quick start guide 1](https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/)
* [Python flask application deployment in Heroku - Quick start guide 2](https://www.jcchouinard.com/deploy-a-flask-app-on-heroku/)
* [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python)