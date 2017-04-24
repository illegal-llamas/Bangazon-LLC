from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *

# Create your views here.
class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product types to be viewed or edited.
    Author: Jordan Nelson
    Methods: n/a
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class OrdersViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows orders to be viewed or edited.
    Author: Harper Frankstone
    Methods: n/a
	"""
	queryset = Orders.objects.all()
	serializer_class = OrdersTypeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed or edited.
    Author: Harper Frankstone
    Methods: n/a
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    Author: Jordan Nelson
    Methods: n/a
    """
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    author: Kayla Brewer
    purpose: creates a viewset class to represent the customer table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, 
    by mixing in the behavior of the various mixin classes.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    
class ComputerTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited
    Author: Nick Nash
    Methods: n/a
    """
    queryset = ComputerType.objects.all()
    serializer_class = ComputerTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

