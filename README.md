# Deploy my website by Heroku
 
 My website: https://khoivn.herokuapp.com
 
 First of all, I want to especially thank Mr. Chau from How Kteam community for providing detailed instructions on Youtube about this blog project. Besides, I also refer to the implementation process on the website of the Corey Schafer Youtube channel
 
 
## Usage

Install heroku:
```bash
pip install --classic heroku
```

Login heroku and change directory to deploy-website-heroku:
```bash
heroku login

cd deploy-website-heroku

heroku create
```

Install all packages in local machine:
```bash
python requirement.txt
```

In my website, I use git of heroku and it is the same with Github. 
```bash
git init

git add . 

git commit -m "message commit"
```

### Deploying code
```bash
git push heroku main
```

### And enjoy to your website by [nameofdatabase].herokuapp.com
