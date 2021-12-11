import base64
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .serializers import OrdersSerializer
from orders.models import Orders
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

def isBasicAuthenticated(view):
    def apiDecorator(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)

        if "HTTP_AUTHORIZATION" in request.META:
            # В заголовке basic-авторизации две части, разделенных пробелом.
            auth = request.META["HTTP_AUTHORIZATION"].split()
            print(auth[1])
            # Первая — слово "Basic"
            if len(auth) == 2 and auth[0].lower() == "basic":
                # Затем base64-кодированные имя пользователя и пароль,
                # разделенные (после декодирования) двоеточием.
                auth_str = auth[1].encode('utf-8')
                decoded = base64.b64decode(auth_str).decode('utf-8')
                username, password = decoded.split(":")
                #username, password = base64.b64decode(auth[1]).split(":")
                # Их и используем с django.contrib.auth.authenticate
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    print("User does not exist")
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        request.user = user
                        return view(request, *args, **kwargs)

        # Если не авторизовали — даем ответ с 401, требуем авторизоваться
        response = HttpResponse()
        response.status_code = 401
        response['WWW-Authenticate'] = 'Basic realm="API"'
        return response

    return apiDecorator

@isBasicAuthenticated
@api_view(['GET'])
def getOrders(request):
    orders = Orders.objects.all()
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@isBasicAuthenticated
@api_view(['GET'])
def getOrder(request, pk):
    order = Orders.objects.get(id=pk)
    serializer = OrdersSerializer(order, many=False)
    return Response(serializer.data)

