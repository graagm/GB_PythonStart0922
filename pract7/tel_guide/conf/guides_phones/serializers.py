from rest_framework import serializers
from .models import UsersPhone, Students

class UsersPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersPhone
        fields = ['id', 'user_name', 'phone_number', 'email']


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'user', 'corse', 'facultet', 'budjet']
