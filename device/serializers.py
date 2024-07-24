from rest_framework import serializers
from .models import Device

class serializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
