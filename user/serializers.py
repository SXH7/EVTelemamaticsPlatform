from rest_framework import serializers
from .models import Customer, CustomerUser

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    

    def validate_customer_zipcode(self, value):
        if len(str(value)) != 6:
            raise serializers.ValidationError("Zipcode must be 6 digits.")

    def validate_customer_phone(self, value):
        if len(str(value)) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits.")


class cuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        exclude = ('cuser_superuser',)
