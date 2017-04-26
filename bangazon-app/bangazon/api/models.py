#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


class ProductType(models.Model):

    """
    Author: Jordan Nelson
    Properties:Creates table "ProductType" with the column product_type_name, 
    the __str__ method makes the product_type_name available to be used in a later foreign key constraint
    """

    product_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_type_name


class Customer(models.Model):

    """ 
    author: Kayla Brewer
    purpose: defines properties associated with the customer object
    properties: first_name, customer_last_name, active, customer_since, 
    the __str__ method makes the first_name available to be used in a later foreign key constraint
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    customer_since = models.DateField(auto_now_add=True)

    def __str__(self):
        """author: Casey Dailey
           purpose: return human readable sting representation of class instance object
           args: 'self', instance of paymentType object
        """
        return self.first_name


# employee payment type:

class CustomerPaymentType(models.Model):

    """ author: Casey Dailey
        purpose: defines properties associated with the customers payment type
        properties:paymentTypeAccountNumber=integer, associated with whatever payment method account used
        paymentTypeName=string, name of given payment type (credit, debit, gift card)
        customerID=integer, foreign key from customer table establishes the relationship between customer and payment type
        methods: __str__
    """

    account_number = models.IntegerField()
    payment_type_name = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer)

    def __str__(self):
        """author: Casey Dailey
           purpose: return human readable sting representation of class instance object
           args: 'self', instance of PaymentType object
        """
        return self.payment_type_name


class Product(models.Model):

    """author: the Nick Nash
    purpose: defines properties associated with the products that customers create
    properties: productTypeID=integer, associated with the foreign key from the ProductType table
    customer=integer,foreign key from the Customer table
    product_name=string, specific product's name
    product_price=float, specific product's price
    product_description=string, associated with the specific product's description
    methods: __str__
    """

    product_type = models.ForeignKey(ProductType)
    customer = models.ForeignKey(Customer)
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

    def __str__(self):
        """author: the Nick Nash
           purpose: return human readable sting representation of class instance object
           args: 'self', instance of productName object
        """
        return self.product_name


class Order(models.Model):

    """author: Harper Franktone
       purpose: defines properties associated with the Orders 
       properties: customerId = relates the orders table to the Customer table through a Foreign Key, 
        paymentTypeId = relates the orders table to the PaymentType table through a foreign key, 
        product_id = relates this table to the Product table through a foreign key
    """

    customer = models.ForeignKey(Customer)
    payment_type = models.ForeignKey(CustomerPaymentType)
    product_name = models.ForeignKey(Product)


class Department(models.Model):

    """author: Harper Frankstone
       purpose: defines properties associated with the Departments
       properties: departmentName = builds the department name column in the department table, departmentBudget = builds the department budget column for the the department table, the __str__ method makes the departmentName available to be used in a later foreign key constraint
    """

    name = models.CharField(max_length=100)
    budget = models.IntegerField()

    def __str__(self):
        """author: Harper Frankstone
           purpose: return human readable sting representation of class instance object
           args: 'self', instance of Department object
        """
        return self.name


class Employee(models.Model):
    """
    Author: Jordan Nelson
    Properties:
    Creates table "EmployeeType" with a foreign key 'departmentID'
    and columns: employee_first_name, employee_last_name, employee_title, employee_pay
    and supervisor. the __str__ method makes the employee_first_name available to be used in a later foreign key constraint
    """
    department = models.ForeignKey(Department)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    pay = models.CharField(max_length=100)
    supervisor = models.BooleanField(default=False)

    def __str__(self):
        """author: Harper Frankstone
           purpose: return human readable sting representation of class instance object
           args: 'self', instance of Employee object
        """
        return self.first_name


class Computer(models.Model):
    """author: Nick Nash
    purpose: defines properties associated with the employee's computer table
    properties: computerPurchaseDate=string, associated with when the computer was purchased
    computerDecomissionDate=string, assocatied with if the computer was decomissioned  
    """
    purchase_date = models.CharField(max_length=50)
    decomission_date = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, blank=True, null=True)


class TrainingProgram(models.Model):
    """author: Harper Frankstone
       purpose: defines properties associated with the TrainingProgram
       properties: program_name,start_date, end_date, max_attendees
    """
    program_name = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    max_attendees = models.IntegerField()


class CustomerSupport(models.Model):
    """author: the Nick Nash
    purpose: defines properties associate with the customer support provided to customers with issues
    properties: 
    customer=integer, id from Customer table
    order=integer, id from Order table
    ticket_description=string, specific customer's reported issue
    date_ticket_created=string, date the customer reported the issue
    resolution_description=string, associated with the resolved issue's description
    date_ticket_resolved=string, associated with the date the customer's issue was resolved
    """
    customer = models.ForeignKey(Customer)
    order = models.ForeignKey(Order)
    ticket_description = models.CharField(max_length=100)
    date_ticket_created = models.CharField(max_length=50)
    resolution_description = models.CharField(max_length=250)
    date_ticket_resolved = models.CharField(max_length=50)

class ProductOrder(models.Model):

    """auth: Jordan Nelson
    purpose: A table created for the purpose querying between the Product and Order tables
    properties:
    Product = Foreign Key to the table Id of the Product table
    Order = Foreign Key to the table Id of the Order table
    """

    product = models.ForeignKey(Customer)
    order = models.ForeignKey(Order)

            