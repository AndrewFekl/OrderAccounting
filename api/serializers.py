from rest_framework import serializers
from orders.models import Orders, Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    #customer = CustomerSerializer(many=False)
    customer = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = Orders
        fields = '__all__'



