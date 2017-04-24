from django.db import models

# Create your models here.
class ProductType(models.Model):
	producttypename = models.CharField(max_length=100)

class Orders(models.Model):
	# customerid = model.ForeignKey(Customer)
	# paymenttypeid = models.ForeignKey(PaymentType)