from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models

class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """list of api features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most controll over your application logic',
            'is mapped manual to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )  

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({"method": 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]

        return Response({"message": "hello!", "a_viewset": "a_viewset"})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"hello {name}!"
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({"http_method": "GET"})
    
    def update(self, request, pk=None):
        """handle updating an pbject"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """updating part of an object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """handle removing an object"""
        return Response({"http_method": "DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()