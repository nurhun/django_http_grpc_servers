from typing import List
from rest_framework import views
from .models import Member
from .serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404


# There are three types of views
# 1- Function-Based view
# 2- Class-Based view
# 3- Viewsets

# 1- Function-Based view
@api_view()
def memberList(request):
    all_members = Member.objects.all()
    data = MemberSerializer(all_members, many=True).data
    return Response({'data': data})

@api_view(['GET',])
def memberGet(request, id):
    get_member = Member.objects.get(id=id)
    data = MemberSerializer(get_member).data
    return Response({'data': data})


# 2- Class-Based view
class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # member = Member
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'id'

# 3- Viewsets
class MemberViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Member.objects.all()
        member = get_object_or_404(queryset, pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Member.objects.all()
        member = get_object_or_404(queryset, pk=pk)
        do = member.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

    # """
    # Example empty viewset demonstrating the standard
    # actions that will be handled by a router class.

    # If you're using format suffixes, make sure to also include
    # the `format=None` keyword argument for each action.
    # """

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass