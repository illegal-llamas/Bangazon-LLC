#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *


# Create your views here.

class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product types to be viewed or edited.
    Author: Jordan Nelson
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer

    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer



class CustomerPaymentTypeViewSet(viewsets.ModelViewSet):
    """
    author: casey dailey
    purpose: creates a viewset class to represent custmer payment type information
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
    """
    queryset = CustomerPaymentType.objects.all()
    serializer_class = CustomerPaymentTypeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    Author: Harper Frankstone
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
 
    """
    queryset = Order.objects.all()
    serializer_class = OrderTypeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed or edited.
    Author: Harper Frankstone
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
 
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    Author: Jordan Nelson
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer

    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    author: Kayla Brewer
    purpose: creates a viewset class to represent the customer table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer

    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited
    Author: Nick Nash
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
 
    """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    author: Harper Frankstone
    purpose: creates a viewset class to represent the training programs table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TrainingProgramViewSet(viewsets.ModelViewSet):
    """
    author: Harper Frankstone
    purpose: creates a viewset class to represent the training programs table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
     """
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer


class CustomerSupportViewSet(viewsets.ModelViewSet):
    """author: Nick Nash
    purpose: creates a viewset class to represent the customer support table created
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
 
    """
    queryset = CustomerSupport.objects.all()
    serializer_class = CustomerSupportSerializer



            