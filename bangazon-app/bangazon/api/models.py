from django.db import models

# Create your models here.
class ProductType(models.Model):
	'''
	Author: Jordan Nelson
	Properties:
	Creates table "ProductType" with the column producttypename
	'''
	producttypename = models.CharField(max_length=100)



#employee payment type:
class CustomerPaymentType(models.Model):
	'''	author: Casey Dailey
		purpose: 
		defines properties associated with the customers payment type
	   	properties:
		paymentTypeAccountNumber=integer, associated with whatever payment method account used
		paymentTypeName=string, name of given payment type (credit, debit, gift card)
		customerID=integer, foreign key from customer table establishes the relationship between customer and payment type
	'''
	paymentTypeAccountNumber = models.IntegerField()
	paymentTypeName = models.CharField(max_length=50)
	#customerID = models.ForeignKey(Customer)



class Orders(models.Model):
	# customerId = models.ForeignKey(Customer)
	# paymentTypeId = models.ForeignKey(PaymentType)
	pass 

class Department(models.Model):
	departmentName = models.CharField(max_length=100)
	departmentBudget = models.IntegerField()

class EmployeeType(models.Model):
	'''
	Author: Jordan Nelson
	Properties:
	Creates table "EmployeeType" with a foreign key 'departmentID'
	and columns: employeeFirstName, employeeLastName, employeeTitle, employeePay
	and supervisor.
	'''
#	departmentID = models.ForeignKey(Department)
	employeeFirstName = models.CharField(max_length=100)
	employeeLastName = models.CharField(max_length=100)
	employeeTitle = models.CharField(max_length=100)
	employeePay = models.CharField(max_length=100)
	supervisor = models.CharField(max_length=100)


class ComputerType(models.Model):
	computerPurchaseDate = models.CharField(max_length=50)
	computerDecomissionDate = models.CharField(max_length=50)


class Customer(models.Model):
    """	
    author: Kayla Brewer
    purpose: defines properties associated with the customer object
    properties: customerFirstName, customerLastName, active, customerSince
	"""
    customerFirstName = models.CharField(max_length=100)
    customerLastName = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    customerSince = models.DateField(auto_now_add=True)

