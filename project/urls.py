"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from . import views
import account_pb2_grpc
from account.services import UserService

urlpatterns = [
    # url(r'^$', views.index_redirect, name='index_redirect'),
    path('', views.index_redirect, name='index_redirect'),
    # url(r'^crud/', include('crud.urls')),
    path('crud/', include('crud.urls')),
    # url(r'^admin/', admin.site.urls),
    # url('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    # url('', include('django_prometheus.urls')),
    path('', include('django_prometheus.urls')),
    path('api-auth/', include('rest_framework.urls')),]


def grpc_handlers(server):
    account_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)