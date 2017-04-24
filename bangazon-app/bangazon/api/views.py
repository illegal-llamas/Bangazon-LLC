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

class EmployeeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer