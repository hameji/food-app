# food-app

This is a app from udemy Mastering django course.

https://www.udemy.com/course/django-course/learn/lecture/14095928?start=645#overview

First you need to make the app to a certain degree.<br>
You need to use venv.<br>
And then setup git with remote github.

Deploy to heroku (need $5/month for database)

Python version has to be the following<br>
https://devcenter.heroku.com/articles/python-support
- 3.12.2 (not supported by pyenv)
- 3.11.8 (not supported by pyenv)
- 3.10.13 = OK ... used this version
- 3.9.18

---
<p>

example from python-3.10.13<br>
**requirements.txt file** 
```
asgiref==3.7.2
dj-database-url==2.1.0
Django==5.0.2
sqlparse==0.4.4
typing_extensions==4.9.0
whitenoise==6.6.0
```

---

## Deployment

There are two(three) ways you can manage deploying to Heroku

- Completely from Heroku HP
- Mixture of both
- local terminal (VSCode/Cursor)

### From Heroku HP 

### Create new project.

From Heroku HP dashboard make a new project.

### Install Heroku CLI

You need to use Heroku CLI to integrate 
```
$ brew tap heroku/brew && brew install heroku
```

### Recognition for Python app

It needs one of the following files.
- requirements.txt
- setup.py
- Pipfile

The easiest one would be requirements.txt

You just have to execute
```
pip install gunicorn # for WSGI Python HTTP server
pip install django-heroku
pip freeze > requiremtents.txt
```
at the root of your project.

Next, set python version 
```
python --version > runtime.txt
```
The file content would be 'Python 3.10.13'
You should manually change it to small letter and add '-' between python and version number.


3. make Procfile

```
echo web: gunicorn mysite.wsgi --log-file - > Procfile
```

### Database

In Heroku sqlite3 is not allowed.
You need to use Postgresql or MySQL as a database.
In Heroku Postgresql is official add-on but MySQL is third-party add-on.

From the Heroku HP console, select 'Resources' tab, and in add-ons section, input Heroku-Postgre and submit.

get details from that link and set it to detail.

### Configure setting.py

Change setting.py to DEPLOYMENT setting.

```
# added at top
import dj_database_url 

# debug
DEBUG = False

# allowed_hosts
ALLOWED_HOSTS = [
    '127.0.0.1', # for local server
    'food-app-9aa86c7affe0.herokuapp.com' # for Heroku server
]

# middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # added

# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # change this
        'HOST': 'ec2-34-236-199-229.compute-1.amazonaws.com', # from Heroku add-on Postgresql
        'NAME': 'dbkf60bgogpmc2', # from Heroku add-on Postgresql
        'USER': 'zokaccsmfnjenx', # from Heroku add-on Postgresql
        'PORT': '5432', # from Heroku add-on Postgresql
        'PASSWORD': '95f314699ef8e960b0d80d93465d6a2a7ef2bd4a3c3ce6bd3a88e9ba5360a21b', # from Heroku add-on Postgresql
    }
}

# static
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# At the end
if not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY']
    import django_heroku
    django_heroku.settings(locals())

    db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(db_from_env)
```

As you can see in the last section, 'SECRET_KEY' is read from os.environ() function.<br>
You need to set environment variable in Heroku server.


```
heroku config:set SECRET_KEY="pass"
```

You can configure this manually on HP.


### Make local_settings.py

You can set this up so that you can run local server when working on local machine.

```
# Add this just before the last section. (if not DEBUG: block)
try:
    from .local_settings import *
except ImportError:
    pass

```

And make local_setting.py file

```
import os
from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-******'

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
```

This would allow sqlite3 in local machine.



### Connect heroku git as remote (to run Heroku CLI)

Need this to run Heroku CLI

```{Terminal}
% git add .
% git commit -m "deploy to heroku"
% heroku git:remote -a ProjectName
```

Once connected, you can use heroku command to the project.

### Heroku CLI commands

0. Login
    ```
    heroku login
    ```

1. Push local branch to Heroku
    ```
    git push heroku main
    ```
    You need to push to heroku git to run the below command.

2. Migrate models
    ```
    heroku run python manage.py migrate
    ```
    heroku run only runs the Heroku(Remote files)
    So you need to push to heroku everytime

3. To see the app running
    ```
    heroku open
    ```
   


## Open heroku server bash (like ssh)

I would recommend the following.
Connect to Heroku with heroku run bash.
Then you don't need to open hp everytime,
don't need to push to heroku git and github and get mixed up.

1. setup github connection

This would allow Heroku to deploy every time there is a merge to a specific branch.

Depending on repository workflow model
- git-flow<br>
  uses 5 branches(main, hotfix, release, develop, feature)
- github-flow<br>
  simple, uses only 2 branch(main + feature)

usually connect to main branch.

To start
```
heroku run bash
```

Run command
```
python manage.py migrate
```

This way you don't need to push to heroku remote and run below everytime
```
heroku run python manage.py migrate
```

To end type
```
exit
```