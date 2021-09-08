from datetime import datetime
from rest_framework import serializers
from .models import CustomUser, SecretMessage


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ['email', 'password']


class SecretMessagesSerializer(serializers.ModelSerializer):
    # user_name = CustomUserSerializer(read_only=True)
    user_name = serializers.SerializerMethodField()
    # secret_id = serializers.UUIDField()
    class Meta:
        model = SecretMessage
        fields = ['secret_id', 'message_name', 'cipher_text', 'decrypt_key', 'user_name']

    def get_user_name(self, obj):
        # print('getuser')
        # request = self.context['request']
        # print(request)
        # return request.user 
        return obj.user_name.username

    def create(self, validated_data):
        print('createSerializer')
        request = self.context.get('request')
        secret_message = SecretMessage()
        secret_message.message_name = validated_data['message_name']
        secret_message.cipher_text = validated_data['cipher_text']
        secret_message.decrypt_key = validated_data['decrypt_key']
        secret_message.user_name = request.user
        secret_message.save()
        return secret_message


class CustomUserSerializer(serializers.ModelSerializer):
    secretmessages = SecretMessagesSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'secretmessages']
