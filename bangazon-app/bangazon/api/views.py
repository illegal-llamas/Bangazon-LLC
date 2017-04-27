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


    queryset = ProductType.objects.order_by('product_type_name')
    serializer_class = ProductTypeSerializer



class CustomerPaymentTypeViewSet(viewsets.ModelViewSet):
    """
    author: casey dailey
    purpose: creates a viewset class to represent custmer payment type information
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
    """


    queryset = CustomerPaymentType.objects.order_by('payment_type_name')
    serializer_class = CustomerPaymentTypeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    Author: Harper Frankstone
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
...."""

    queryset = Order.objects.order_by('product_name')
    serializer_class = OrdersSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed or edited.
    Author: Harper Frankstone
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
 
    """


    queryset = Department.objects.order_by('name')
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    Author: Jordan Nelson
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer

    """


    queryset = Employee.objects.order_by('first_name')
    serializer_class = EmployeeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    author: Kayla Brewer
    purpose: creates a viewset class to represent the customer table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer

    """


    queryset = Customer.objects.order_by('first_name')
    serializer_class = CustomerSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited
    Author: Nick Nash
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
 
    """


    queryset = Computer.objects.order_by('purchase_date')
    serializer_class = ComputerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    author: Harper Frankstone
    purpose: creates a viewset class to represent the training programs table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer

    """


    queryset = Product.objects.order_by('product_name')
    serializer_class = ProductSerializer


class TrainingProgramViewSet(viewsets.ModelViewSet):
    """
    author: Harper Frankstone
    purpose: creates a viewset class to represent the training programs table
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
    """

    queryset = TrainingProgram.objects.order_by('program_name')
    serializer_class = TrainingProgramSerializer


class CustomerSupportViewSet(viewsets.ModelViewSet):
    """author: Nick Nash
    purpose: creates a viewset class to represent the customer support table created
    args: viewsets.ModelViewSet, see docs @ http://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    properties: queryset=specifies the model and query parameters
                serializer_class=specifies the corresponding serializer
 
    """

    queryset = CustomerSupport.objects.order_by('date_ticket_created')
    serializer_class = CustomerSupportSerializer
