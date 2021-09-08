from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import SignupSerializer, CustomUserSerializer, SecretMessagesSerializer
from rest_framework.permissions import AllowAny
from .models import CustomUser, SecretMessage


class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            print(serializer.validated_data)
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            CustomUser.objects.create_user(email=email, password=password)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class SecretMessagesList(generics.ListCreateAPIView):
    serializer_class = SecretMessagesSerializer

    def perform_create(self, serializer):        
        print('createview')
        serializer.save()

    def get_queryset(self):
        user = self.request.user
        return SecretMessage.objects.filter(user_name=user)


class SecretMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SecretMessagesSerializer
    lookup_field = 'secret_id'

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        user = self.request.user
        return SecretMessage.objects.filter(user_name=user)
