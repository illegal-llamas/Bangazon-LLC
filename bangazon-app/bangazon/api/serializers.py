from rest_framework import serializers
from bangazon.api.models import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        exclude = ()

class CustomerPaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    '''author: casey dailey
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    '''
    class Meta:
        '''author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        '''
        model = CustomerPaymentType
        exclude = ()

