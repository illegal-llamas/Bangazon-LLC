from django.db import models

# Create your models here.
class ProductType(models.Model):
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
