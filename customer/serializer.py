from rest_framework import serializers
from .models import *



class customerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['custId', 'custFname', 'custLname', 'custEmail','custPhone', 'address', 'product', 'expiryDate','amount','itemQuantity', 'technition', 'message', 'createdAt']
        read_only_fields = ['custId','createdAt']


class customerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['custId', 'custFname', 'custLname', 'custEmail','custPhone', 'address', 'product', 'expiryDate','itemQuantity', 'amount', 'technition', 'message', 'createdAt']
        read_only_fields = ['custId','createdAt']
        depth = 2