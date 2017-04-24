from rest_framework import viewsets
from bangazon.api.serializers import *
from bangazon.api.models import *

# Create your views here.
class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product types to be viewed or edited.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class OrdersViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows orders to be viewed or edited.
	"""
	queryset = Orders.objects.all()
	serializer_class = OrdersTypeSerializer