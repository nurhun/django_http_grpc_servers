from rest_framework import routers, serializers, viewsets
from .models import Member


# Serializers define the API representation.
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        # fields = ['firstname', 'lastname']
        fields = '__all__'

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]