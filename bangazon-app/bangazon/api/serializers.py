from rest_framework import serializers
from bangazon.api.models import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        exclude = ()

class OrdersTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Orders
		exclude = ()

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Department
		exclude = ()