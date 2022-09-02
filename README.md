# **Rest Api User-agent-Random**
<p align="center">
<img src="https://avatars.githubusercontent.com/Xenzi-XN1" width="200" height="200"/>
</p>
<p align="center">
  <a href="#"><img src="http://readme-typing-svg.herokuapp.com?color=d1fa02&center=true&vCenter=true&multiline=false&lines=Welcome+To+Api+User-agent-Random" alt="">
</p>
<p align="center">
<a href="https://github.com/Xenzi-XN1"><img title="Creator" src="https://img.shields.io/badge/Creator-Xenzi-green.svg?style=for-the-badge&logo=github"></a>
</p>
simple Rest-API User-agent-Random menggunakan flask

## Cloning this repo
```cmd
> git clone https://github.com/Xenzi-XN1/Api-User-Agent-Random
> cd Api-User-Agent-Random
```

## Run Rest-API
```cmd
> pip install -r requirements.txt
> python app.py
```

<img src="https://i.ibb.co/HqK1FbQ/IMG-20220902-154034.jpg" width="500">

# Tutorial
Rest-API User-agent-Random ini menggunakan metode `GET`
```cmd
http://127.0.0.1:5000/api/user-agent-random
```

<img src="https://i.ibb.co/BLtwjw9/IMG-20220902-154048.jpg" width="500">

Menggunakan `python`
```python
import requests
data = requests.get('http://127.0.0.1:5000/api/user-agent-random').text
print (data)
```
Status data
```json
{
    "status": "success",
    "user_agent_random": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "developer": "Xenzi Ganz",
    "github_admin": "https://github.com/Xenzi-XN1"
}
```
# Deploy Heroku

Go to [Heroku](https://heroku.com) and Login

Create New App ( App Name For Example : abcd-api)

<img src="https://i.postimg.cc/Z5T8Btw2/newapp.png" width="500">

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

Open `CMD` and Login Heroku

```cmd
> heroku login
```

Initialize a git repository in a new or existing directory

```cmd
> cd Api-User-Agent-Random
> git init
```

Remote Your App, Use `heroku git:remote -a app-name`

```cmd
> heroku git:remote -a abcd-api
```

Commit your code to the repository and deploy it to Heroku using Git.

```cmd
> git add .
> git commit -am "make it better"
> git push heroku master
```

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/)

