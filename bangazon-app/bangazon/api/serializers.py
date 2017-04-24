from rest_framework import serializers
from bangazon.api.models import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        exclude = ()

class EmployeeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeType
        exclude = ()