from rest_framework import serializers
from .models import *
from product.models import product
from product.serializer import productWriteSerializer,productReadSerializer

class vendorWriteSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = VendorMaster
        fields = ['createdAt','vendorId','vendorCode','vendorName','vendorAddress','vendorPrimaryEmail','vendorPrimaryPhone','vendorPrimaryName','vendorSecondaryEmail','vendorSecondaryPhone','products']
        read_only_fields = ['createdAt','vendorId']
      


class orderWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'


class orderReceivedWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderReceived
        fields = '__all__'
        dept = 2

class vendorReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VendorMaster
        fields = ['createdAt','vendorId','vendorCode','vendorName','vendorAddress','vendorPrimaryEmail','vendorPrimaryPhone','vendorPrimaryName','vendorSecondaryEmail','vendorSecondaryPhone','products']
        read_only_fields = ['createdAt','vendorId']
        depth = 2


class orderReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        dept = 1

class orderReceivedReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderReceived
        fields = '__all__'
        dept = 2