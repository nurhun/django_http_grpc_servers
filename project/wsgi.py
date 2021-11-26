"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from typing import List

from django.core.wsgi import get_wsgi_application
from grpcWSGI.server import grpcWSGI
import account_pb2_grpc

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()
application = grpcWSGI(application)

# https://github.com/public/sonora
account_pb2_grpc.add_UserControllerServicer_to_server(account_pb2_grpc.UserControllerServicer(), application)