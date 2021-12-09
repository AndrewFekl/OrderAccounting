from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('order/<str:pk>/', views.single_order, name='single-order'),
    path('create-order/', views.createOrder, name='create-order'),
    path('update-order/<str:pk>', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>', views.deleteOrder, name='delete-order'),
]
