from rest_framework import serializers
from bangazon.api.models import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """author: Jordana mr. Nelson
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        """author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = ProductType
        exclude = ()

class CustomerPaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """author: casey dailey
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        """author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = CustomerPaymentType
        exclude = ()


class OrdersTypeSerializer(serializers.HyperlinkedModelSerializer):
    """author: casey dailey
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
	class Meta:
        """author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
		model = Orders
		exclude = ()

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """author: casey dailey
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
	class Meta:
        """author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
		model = Department
		exclude = ()

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Kayla Brewer
    purpose: specify model and fields to include (here we include all) from the customer table
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        """author: Kayla Brewer
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Employee
        exclude = ()


class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Kayla Brewer
    purpose: specify model and fields to include (here we include all) from the customer table
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        """author: Kayla Brewer
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Customers
        exclude = ()

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    """author: Nick Nash
    purpose: extends the parent serializer class with validators specifying the model and fields to exclude (here we include all)
    args: n/a
    docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
    """
    class Meta:
        """author: Nick the Nash
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Computer
        exclude = ()
		
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """author: Nick Nash
    purpose: extends the parent serializer class with validators specifying the model and fields to exclude (here we include all)
    args: n/a
    docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
    """
    class Meta:
        """author: Nick the Nash
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Product
        exclude = ()

class TrainingProgramsSerializer(serializers.HyperlinkedModelSerializer):
    """author: Harper Frankstone
    purpose: extends the parent serializer class with validators specifying the model and fields to exclude (here we include all)
    args: n/a
    docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
    """
    class Meta:
        """author: Harper Frankenstein
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        args: n/a
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = TrainingPrograms
        exclude = ()

# class CustomerSupportSerializer(serializers.HyperlinkedModelSerializer):
#     """author: Nick Nash
#     purpose: extends the parent serializer class with validators specifying the model and fields to exclude (here we include all)
#     args: n/a
#     docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance
#     """
#     class Meta:
#         """author: Nick the Nash
#         purpose: extends the parent serializer class with validators 
#         specifying the model and fields to exclude (here we include all)
#         args: n/a
#         docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
#         """
#         model = CustomerSupport
#         exclude = ()
        
