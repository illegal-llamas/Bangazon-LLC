from rest_framework import serializers
from bangazon.api.models import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: casey dailey
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """

    class Meta:
        """
        author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)
                    
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = ProductType
        exclude = ()

class CustomerPaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: casey dailey
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """

    class Meta:
        """
        author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)
                    
        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = CustomerPaymentType
        exclude = ()


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: casey dailey
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        """
        author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)

        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Order
        exclude = ()

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: casey dailey
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        """
        author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)

        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Department
        exclude = ()

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: casey dailey
    purpose: specify model and fields to include (here we include all)
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        """
        author: casey dailey
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)

        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Employee
        exclude = ()


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    author: Kayla Brewer
    purpose: specify model and fields to include (here we include all) from the customer table
    args: serializers.HyperlinkedModelSerializer, see docs @ http://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer 
    uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        """
        author: Kayla Brewer
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)

        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Customer
        exclude = ()

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """
        author: Kayla Brewer
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)

        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Computer
        exclude = ()
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """
        author: Nick Nash
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)

        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = Product
        exclude = ()

class TrainingProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """
        author: Harper Frankstone
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)

        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = TrainingProgram
        exclude = ()

class CustomerSupportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """
        author: Nick Nash
        purpose: extends the parent serializer class with validators 
        specifying the model and fields to exclude (here we include all)
        properties: model = specifies the model to be serialized
                    exclude = specifies fields to be included (here we exclude none)

        docs: http://www.django-rest-framework.org/api-guide/serializers/#serializer-inheritance 
        """
        model = CustomerSupport
        exclude = ()
        

            
            
            