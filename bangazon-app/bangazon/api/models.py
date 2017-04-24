from django.db import models

# Create your models here.
class ProductType(models.Model):
	producttypename = models.CharField(max_length=100)


class Orders(models.Model):
	# customerId = models.ForeignKey(Customer)
	# paymentTypeId = models.ForeignKey(PaymentType)
	pass 

class Department(models.Model):
	departmentName = models.CharField(max_length=100)
	departmentBudget = models.IntegerField()

class EmployeeType(models.Model):
#	departmentID = models.ForeignKey(Department)
	employeeFirstName = models.CharField(max_length=100)
	employeeLastName = models.CharField(max_length=100)
	employeeTitle = models.CharField(max_length=100)
	employeePay = models.CharField(max_length=100)
	supervisor = models.CharField(max_length=100)

class ComputerType(models.Model):
	computerPurchaseDate = models.CharField(max_length=50)
	computerDecomissionDate = models.CharField(max_length=50)

