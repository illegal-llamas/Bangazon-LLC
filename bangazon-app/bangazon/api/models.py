from django.db import models

# Create your models here.
class ProductType(models.Model):
	producttypename = models.CharField(max_length=100)

class EmployeeType(models.Model):
#	departmentID = models.ForeignKey(Department)
	employeeFirstName = models.CharField(max_length=100)
	employeeLastName = models.CharField(max_length=100)
	employeeTitle = models.CharField(max_length=100)
	employeePay = models.CharField(max_length=100)
	supervisor = models.CharField(max_length=100)

class Customer(models.Model)
    """Create a customer table in the database with the values firstname, lastname, active, and customersince"""
    customerFirstName = models.CharField(max_length=100)
    customerLastName = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    customerSince = models.DateField(auto_now_add=True)