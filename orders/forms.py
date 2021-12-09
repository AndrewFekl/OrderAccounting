from django import forms
from django.forms import ModelForm, widgets
from .models import Orders

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['created', 'description', 'amount', 'customer']

        widgets = {
            'customer': forms.Select(),
            'created': forms.TextInput(attrs={'placeholder': 'Дата Г-М-Д Ч:М:С'}),
            'description': forms.TextInput(attrs={'placeholder': 'Описание заказа'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Стоимость в рублях'}),
        }




