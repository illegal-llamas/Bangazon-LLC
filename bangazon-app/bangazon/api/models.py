from django.db import models

# Create your models here.
class ProductType(models.Model):
	"""
	Author: Jordan Nelson
	Properties: product_type_name
	Creates table "ProductType" with the column producttypename, the __str__ method makes the producttypename available to be used in a later foreign key constraint
	"""
	product_type_name = models.CharField(max_length=100)

	def __str__(self):
		return self.product_type_name 

class Customers(models.Model):
    """ 
    author: Kayla Brewer
    purpose: defines properties associated with the customer object
    properties: customer_first_name, customer_last_name, active, customer_since, 
    the __str__ method makes the customerFIrstName available to be used in a later foreign key constraint
    """
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    customer_since = models.DateField(auto_now_add=True)

    def __str__(self):
    	return self.customer_first_name

#employee payment type:
class CustomerPaymentType(models.Model):
    """ author: Casey Dailey
        purpose: defines properties associated with the customers payment type
        properties:paymentTypeAccountNumber=integer, associated with whatever payment method account used
        paymentTypeName=string, name of given payment type (credit, debit, gift card)
        customerID=integer, foreign key from customer table establishes the relationship between customer and payment type
        the __str__ method makes the paymentTypeName available to be used in a later foreign key constraint
    """
    payment_type_account_number = models.IntegerField()
    payment_type_name = models.CharField(max_length=50)
    customerID = models.ForeignKey(Customers)

    def __str__(self):
    	return self.payment_type_name


class Product(models.Model):
	"""author: Nick Nash
	purpose: defines properties associated with the products that customers create
	properties: productTypeID=integer, associated with the foreign key from the ProductType table
	customerID=integer, associated with the foreign key from the Customer table
	productName=string, associated with the specific product's name
	productPrice=float, associated with the specific product's price
	productDescription=string, associated with the specific product's description
	the __str__ method makes the productName available to be used in a later foreign key constraint
	docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
	"""
	productTypeID = models.ForeignKey(ProductType)
	customerID = models.ForeignKey(Customers)
	product_name = models.CharField(max_length=100)
	product_price = models.CharField(max_length=25)
	product_description = models.CharField(max_length=100)

	def __str__(self):
		return self.product_name


class Orders(models.Model):
    """author: Harper Franktone
       purpose: defines properties associated with the Orders
       properties: customerId = relates the orders table to the Customer table through a Foreign Key, paymentTypeId = relates the orders table to the PaymentType table through a foreign key, product_id = relates this table to the Product table through a foreign key
    """
    customerID = models.ForeignKey(Customers)
    paymentTypeID = models.ForeignKey(CustomerPaymentType)
    product_name = models.ForeignKey(Product)


class Department(models.Model):
    """author: Harper Franktone
       purpose: defines properties associated with the Departments
       properties: departmentName = builds the department name column in the department table, departmentBudget = builds the department budget column for the the department table, the __str__ method makes the departmentName available to be used in a later foreign key constraint
    """
    department_name = models.CharField(max_length=100)
    department_budget = models.IntegerField()

    def __str__(self):
    	return self.department_name

class Employee(models.Model):
	"""
	Author: Jordan Nelson
	Properties:
	Creates table "Employee" with a foreign key 'departmentID'
	and columns: employeeFirstName, employeeLastName, employeeTitle, employeePay
	and supervisor. the __str__ method makes the employeeFirstName available to be used in a later foreign key constraint
	"""
	departmentID = models.ForeignKey(Department)
	employee_first_name = models.CharField(max_length=100)
	employee_last_name = models.CharField(max_length=100)
	employee_title = models.CharField(max_length=100)
	employee_pay = models.CharField(max_length=100)
	supervisor = models.BooleanField(default=False)

	def __str__(self):
		return self.employee_first_name



class Computer(models.Model):
	"""author: Nick Nash
	purpose: defines properties associated with the employee's computer table
	properties: 
	computerPurchaseDate=string, associated with when the computer was purchased
	computerDecomissionDate=string, assocatied with if the computer was decomissioned 
	docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
	"""
	computer_purchase_date = models.CharField(max_length=50)
	computer_decomission_date = models.CharField(max_length=50)
	employee_id = models.ForeignKey(Employee, blank=True, null=True)

class TrainingPrograms(models.Model):
    """author: Harper Franktone
       purpose: defines properties associated with the TrainingProgram
       properties: training_program_name, start_date, end_date, max_attendees
    """
    training_program_name = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    max_attendees = models.IntegerField()

# class CustomerSupport(models.Model):
#     """author: Nick Nash
#     purpose: defines properties associate with the customer support provided to customers with issues
#     properties: 
#     customerID=integer, associated with the foreign key from the Customer table
#     orderID=integer, associated with the foreign key from the Order table
#     ticket_description=string, associated with the specific customer's reported issue
#     date_ticket_created=string, associated with the date the customer reported the issue
#     resolution_description=string, associated with the resolved issue's description
#     date_ticket_resolved=string, associated with the date the customer's issue was resolved
#     """
#     customerID = models.ForeignKey(Customer)
#     orderID = models.ForeignKey(Orders)
#     ticket_description = models.CharField(max_length=100)
#     date_ticket_created = models.CharField(max_length=50)
#     resolution_description = models.CharField(max_length=100)
#     date_ticket_resolved = models.CharField(max_length=50)
