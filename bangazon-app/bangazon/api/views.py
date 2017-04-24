from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *

# Create your views here.
class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

#view to represent customer payment type information
class CustomerPaymentTypeViewSet(viewsets.ModelViewSet):
    '''
    author: casey dailey
    purpose: creates a viewset class to represent custmer payment type information
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, 
    by mixing in the behavior of the various mixin classes.
    '''
    queryset = CustomerPaymentType.objects.all()
    serializer_class = CustomerPaymentTypeSerializer
