### Simple food service api with Django

##### features:
* rest api for foods
* rest api from recipients

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
 - http://localhost:8000/recipients/
 - http://localhost:8000/product-sets/
