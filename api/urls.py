from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.getOrders),
    path('orders/<str:pk>/', views.getOrder),

]
