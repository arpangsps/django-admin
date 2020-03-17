from rest_framework import serializers
from django.db import models
from .models import user_details

class user_detailsSerializer(serializers.Serializer):
    role = serializers.CharField(max_length = 10)
