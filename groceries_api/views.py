from django.shortcuts import render

from rest_framework import viewsets
from groceries_api import serializers, models, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.ProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateOwnProfile,)


class GroceriesViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and update groceries items """


    serializer_class =  serializers.GroceriesItemSerializer
    queryset = models.Groceries.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateOwnGroceries,)


    def perform_create(self, serializer):

        serializer.save(user_profile=self.request.user)



class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
