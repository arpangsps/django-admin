from rest_framework import serializers
from django.db import models
from .models import User

class userSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']   

    def create(self, validated_data):
        return user(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    

