from django.conf.urls import include, url
from django.urls import path

from . import views
from . import api

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/v3/member-viewset', api.MemberViewSet, basename='member-viewset')
# urlpatterns = router.urls

urlpatterns= [
    # HTTP methods
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

    # REST API Function-Based view
    path('api/list/', api.memberList, name='api_list'),
    path('api/get/<int:id>', api.memberGet, name='api_get'),

    # REST API Class-Based view
    path('api/v2/list/', api.MemberList.as_view(), name='api_list_and_create'),
    path('api/v2/updatedestroy/<int:id>', api.MemberUpdateDestroy.as_view(), name='api_update_and_destroy'),

    # REST API viewsets
    path('', include(router.urls)),
]

