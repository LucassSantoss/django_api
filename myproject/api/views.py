from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
class HelloWorld(APIView):
    def get(self, request):
        return Response(status=200, content_type='json', data={'message': 'Hello, World!'})
    
class CreateUser(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)