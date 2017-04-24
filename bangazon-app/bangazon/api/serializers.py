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

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Kayla Brewer
    purpose: specify model and fields to include (here we include all) from the customer table
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        model = Customer
        exclude = ()