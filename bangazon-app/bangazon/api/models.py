from django.db import models

# Create your models here.
class ProductType(models.Model):
	'''
	Author: Jordan Nelson
	Properties:
	Creates table "ProductType" with the column producttypename, the __str__ method makes the producttypename available to be used in a later foreign key constraint
	'''
	producttypename = models.CharField(max_length=100)

	def __str__(self):
		return self.producttypename 

class Customer(models.Model):
    """ 
    author: Kayla Brewer
    purpose: defines properties associated with the customer object
    properties: customerFirstName, customerLastName, active, customerSince, the __str__ method makes the customerFIrstName available to be used in a later foreign key constraint
    """
    customerFirstName = models.CharField(max_length=100)
    customerLastName = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    customerSince = models.DateField(auto_now_add=True)

    def __str__(self):
    	return self.customerFirstName

#employee payment type:
class CustomerPaymentType(models.Model):
    ''' author: Casey Dailey
        purpose: 
        defines properties associated with the customers payment type
        properties:
        paymentTypeAccountNumber=integer, associated with whatever payment method account used
        paymentTypeName=string, name of given payment type (credit, debit, gift card)
        customerID=integer, foreign key from customer table establishes the relationship between customer and payment type
        the __str__ method makes the paymentTypeName available to be used in a later foreign key constraint
    '''
    paymentTypeAccountNumber = models.IntegerField()
    paymentTypeName = models.CharField(max_length=50)
    customerID = models.ForeignKey(Customer)

    def __str__(self):
    	return self.paymentTypeName


class Product(models.Model):
	'''author: Nick Nash
	purpose: defines properties associated with the products that customers create
	properties: 
	productTypeID=integer, associated with the foreign key from the ProductType table
	customerID=integer, associated with the foreign key from the Customer table
	productName=string, associated with the specific product's name
	productPrice=float, associated with the specific product's price
	productDescription=string, associated with the specific product's description
	the __str__ method makes the productName available to be used in a later foreign key constraint
	docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
	'''
	productTypeID = models.ForeignKey(ProductType)
	customerID = models.ForeignKey(Customer)
	productName = models.CharField(max_length=100)
	productPrice = models.CharField(max_length=25)
	productDescription = models.CharField(max_length=100)

	def __str__(self):
		return self.productName


class Orders(models.Model):
    '''author: Harper Franktone
       purpose: defines properties associated with the Orders
       properties: customerId = relates the orders table to the Customer table through a Foreign Key, paymentTypeId = relates the orders table to the PaymentType table through a foreign key, product_id = relates this table to the Product table through a foreign key
    '''
    customerID = models.ForeignKey(Customer)
    paymentTypeId = models.ForeignKey(CustomerPaymentType)
    product_name = models.ForeignKey(Product)


class Department(models.Model):
    '''author: Harper Franktone
       purpose: defines properties associated with the Departments
       properties: departmentName = builds the department name column in the department table, departmentBudget = builds the department budget column for the the department table, the __str__ method makes the departmentName available to be used in a later foreign key constraint
    '''
    departmentName = models.CharField(max_length=100)
    departmentBudget = models.IntegerField()

    def __str__(self):
    	return self.departmentName

class EmployeeType(models.Model):
	'''
	Author: Jordan Nelson
	Properties:
	Creates table "EmployeeType" with a foreign key 'departmentID'
	and columns: employeeFirstName, employeeLastName, employeeTitle, employeePay
	and supervisor. the __str__ method makes the employeeFirstName available to be used in a later foreign key constraint
	'''
	departmentID = models.ForeignKey(Department)
	employeeFirstName = models.CharField(max_length=100)
	employeeLastName = models.CharField(max_length=100)
	employeeTitle = models.CharField(max_length=100)
	employeePay = models.CharField(max_length=100)
	supervisor = models.BooleanField(default=False)

	def __str__(self):
		return self.employeeFirstName

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
	employee_id = models.ForeignKey(EmployeeType, blank=True, null=True)

class TrainingPrograms(models.Model):
    '''author: Harper Franktone
       purpose: defines properties associated with the TrainingProgram
       properties: 
    '''
    trainingProgramName = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    maxAttendees = models.IntegerField()