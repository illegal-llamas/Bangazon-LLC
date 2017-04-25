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


#view to represent customer payment type information
class CustomerPaymentTypeViewSet(viewsets.ModelViewSet):
    """
    author: casey dailey
    purpose: creates a viewset class to represent custmer payment type information
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, 
    by mixing in the behavior of the various mixin classes.
    """
    queryset = CustomerPaymentType.objects.all()
    serializer_class = CustomerPaymentTypeSerializer


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

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    Author: Jordan Nelson
    Methods: n/a
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CustomersViewSet(viewsets.ModelViewSet):
    """
    author: Kayla Brewer
    purpose: creates a viewset class to represent the customer table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, 
    by mixing in the behavior of the various mixin classes.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

    
class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited
    Author: Nick Nash
    Methods: n/a
    """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    author: Nick the Nash
    purpose: creates a viewset class to represent the products table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, 
    by mixing in the behavior of the various mixin classes.

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class TrainingProgramsViewSet(viewsets.ModelViewSet):
    """
    author: Harper Frankstone
    purpose: creates a viewset class to represent the training programs table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, 
    by mixing in the behavior of the various mixin classes.
    """
    queryset = TrainingPrograms.objects.all()
    serializer_class = TrainingProgramsSerializer

# class CustomerSupportViewSet(viewsets.ModelViewSet):
#     """author: Nick Nash
#     purpose: creates a viewset class to represent the customer support table created
#     args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
#     The ModelViewSet class inherits from GenericAPIView and includes implementations for various actions, 
#     by mixing in the behavior of the various mixin classes.
#     """
#     queryset = CustomerSupport.objects.all()
#     serializer_class = CustomerSupportSerializer
