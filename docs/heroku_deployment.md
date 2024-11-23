## Host Website using Heroku

Automatic Deployment from GitHub (Recommended)
------------------------------------
It is recommended to maintain a GitHub repository for your project for version control. You can easily integrate your GitHub repository with Heroku app and deploy your application directly from your GitHub branch. Heroku will build and deploy a new version of application for every push to specified branch.   
You can create a CI/CD pipeline for continous delivery of your application in Heroku dashboard. Refer [here](https://devcenter.heroku.com/articles/pipelines)  

Manual Deployment Using Heroku Repo
-----------------------------

### 1. Prerequisite
* [Heroku Account](https://www.heroku.com/platform)
* [Heroku cli](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)  
Ubuntu installation: `sudo snap install heroku --classic`
* Git

### 2. Deploy Application using Heroku CLI
1. `heroku login`
2. `heroku create markettoday`
3. `git push heroku main` 

Finally, web app will be deployed on https://markettoday.herokuapp.com/ 

## References
* [Python flask application deployment in Heroku - Quick start guide 1](https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/)
* [Python flask application deployment in Heroku - Quick start guide 2](https://www.jcchouinard.com/deploy-a-flask-app-on-heroku/)
* [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python)