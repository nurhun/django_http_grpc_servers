# django_CRUD

CRUD is a simple web based Django project where user can Create, Update and Delete data from database.


## For gRPC

To define the gRPC service and messages, you can generate it automatically based on User model:<br />
$ python manage.py generateproto --model django.contrib.auth.models.User --fields id,username,email,groups --file account.proto

Reference: https://djangogrpcframework.readthedocs.io/en/latest/quickstart.html
