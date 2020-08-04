Simple food service api with Django
==================  
[![Heroku](https://heroku-badge.herokuapp.com/?app=food-api-service&style=flat)](https://food-api-service.herokuapp.com)

##### features:
* rest api for order food

##### requirements:
 - Python 3.6+
 - Django 3
 - Gunicorn 20+
 - Django Rest Framework 3.11

##### install requirements:
`pip3 install -r requirements.txt`

##### run tests:
`python manage.py test`

##### run app:
 - `python manage.py migrate`
 - `python manage.py import_data`
 - `gunicorn food_project.wsgi`

##### usage:
 - swagger http://127.0.0.1:8000/
 - admin http://127.0.0.1:8000/admin/ (admin/admin)
