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

class ComputerType(models.Model):
	'''author: Nick Nash
	purpose: defines properties associated with the employee's computer table
	properties: 
	computerPurchaseDate=string, associated with when the computer was purchased
	computerDecomissionDate=string, assocatied with if the computer was decomissioned 
	docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
	'''
	computerPurchaseDate = models.CharField(max_length=50)
	computerDecomissionDate = models.CharField(max_length=50)

class Product(models.Model):
	'''author: Nick Nash
	purpose: defines properties associated with the products that customers create
	properties: 
	productTypeID=integer, associated with the foreign key from the ProductType table
	customerID=integer, associated with the foreign key from the Customer table
	productName=string, associated with the specific product's name
	productPrice=float, associated with the specific product's price
	productDescription=string, associated with the specific product's description
	docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
	'''
	# productTypeID = models.ForeignKey(ProductType)
	# customerID = models.ForeignKey(Customer)
	productName = models.CharField(max_length=100)
	productPrice = models.CharField(max_length=25)
	productDescription = models.CharField(max_length=100)
