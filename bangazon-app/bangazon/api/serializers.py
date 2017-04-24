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

class ComputerTypeSerializer(serializers.HyperlinkedModelSerializer):
    '''author: Nick Nash
    purpose: extends the parent serializer class with validators specifying the model and fields to exclude (here we include all)
    args: n/a
    docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
    '''
    class Meta:
        model = ComputerType
        exclude = ()
		
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    '''author: Nick Nash
    purpose: extends the parent serializer class with validators specifying the model and fields to exclude (here we include all)
    args: n/a
    docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
    '''
    class Meta:
        model = Product
        exclude = ()
