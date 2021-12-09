from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('order/<int:pk>/', views.single_order, name='single-order'),
]
