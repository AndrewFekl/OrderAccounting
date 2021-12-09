from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('order/<str:pk>/', views.single_order, name='single-order'),
    path('create-order/', views.createOrder, name='create-order')
]
