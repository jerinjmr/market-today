# Stock Recommendation System  
Website for stock news and recommendations using python web scraping technology. Python flask server is used as back-end service and uses Heroku platform to deploy the web application.  
Visit [JMR Investmensts and Research center](http://jmrinvestments.herokuapp.com.) to view indian stock news and recommendations.  

## Run program locally

### 1. Prerequisite
1. Python3  
2. Pip  

### 2. Install dependencies
`pip3 install -r requirements.txt`

### 3. Run server
`python3 wsgi.py`  
Go to http://127.0.0.1:5000/ to view the results in webpage.

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