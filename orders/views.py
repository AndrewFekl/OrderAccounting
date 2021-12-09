from django.shortcuts import render, redirect
from .models import Orders, Customer
from .forms import OrderForm

def orders(request):
    customer_dict = {}
    orders = Orders.objects.all()
    customers = Customer.objects.all()
    for customer in customers:
        customer_dict[customer.id] = customer.title
    context = {'orders': orders, 'customer_dict': customer_dict}
    return render(request, 'orders/orders.html', context)

def single_order(request, pk):
    order = Orders.objects.get(id=pk)
    context = {'order': order}
    return render(request, 'orders/single_order.html', context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form}
    return render(request, 'orders/order_form.html', context)

def updateOrder(request, pk):
    order = Orders.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form}
    return render(request, 'orders/order_form.html', context)

def deleteOrder(request, pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders')
    context = {'order': order}
    return render(request, 'orders/delete_template.html', context)

