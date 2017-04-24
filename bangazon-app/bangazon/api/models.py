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