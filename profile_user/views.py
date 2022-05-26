from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.response import Response
from profile_user.models import UsersProfile
from rest_framework import status, filters
from profile_user.serializers import UsersSerializer
from rest_framework import viewsets
from profile_user import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated



class UsersViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UsersSerializers
    queryset = models.UsersProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filters_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.UsersProfile = None

    def list(self, request):
        a_viewset = [
            f'{self.UsersProfile.name}, {self.UsersProfile.email}, {self.UsersProfile.rol}'
        ]
        return Response({'message': 'Users', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(dat=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response()
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes: (
        permissions.UpdateOwnStatus,
        IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
