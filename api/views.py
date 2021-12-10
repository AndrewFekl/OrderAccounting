from .serializers import OrdersSerializer
from orders.models import Orders
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getOrders(request):
    orders = Orders.objects.all()
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOrder(request, pk):
    order = Orders.objects.get(id=pk)
    serializer = OrdersSerializer(order, many=False)
    return Response(serializer.data)

