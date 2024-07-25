from rest_framework import serializers
from app1.models import *

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    def validate_age(self, value):
        if value > 18:
            raise serializers.ValidationError('age must be 18 less than')
        return value
    def validate_name(self, value):
        if len(value) > 7:
            raise serializers.ValidationError('name is must be 7 letter less than')
        return value
    

from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
    recipient_list = serializers.ListField(
        child=serializers.EmailField()
    )