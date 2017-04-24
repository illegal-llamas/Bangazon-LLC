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

class ComputerTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited
    Author: Nick Nash
    Methods: n/a
    """
    queryset = ComputerType.objects.all()
    serializer_class = ComputerTypeSerializer

