from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
class HelloAPIView(APIView):
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        api_list=['I am the best',' I am scared a bit', ' I should be scared']
        return Response({'message':'hello','an_apiview':api_list})
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
    def put(self,request,pk=None):
        '''Replace the object'''
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        '''update specified only'''
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        '''Delete Specified object'''
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        api_list=['I am the best',' I am scared a bit', ' I should be scared']
        return Response({'message':'hello me viewset hu','an_apiviewset':api_list})
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello{name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_404_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        return Response({"http-method":"GET"})
    def update(self,request,pk=None):
        return Response({"http-method":"PUT"})
    def partial_update(self,request,pk=None):
        return Response({"http-mehtod":"PATCH"})
    def destroy(self,request,pk=None):
        return Response({"http-method":"DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)
class UserLoginView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)