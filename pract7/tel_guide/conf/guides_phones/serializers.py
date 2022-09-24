from rest_framework import serializers
from .models import UsersPhone

class UsersPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersPhone
        fields = ['id', 'user_name', 'phone_number', 'email']
