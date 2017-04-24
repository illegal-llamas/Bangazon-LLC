from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *

# Create your views here.
class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class EmployeeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer

class ComputerTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited
    """
    queryset = ComputerType.objects.all()
    serializer_class = ComputerTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
