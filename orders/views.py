from django.shortcuts import render, redirect
from .models import Orders, Customer
from .forms import OrderForm, SelectForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
import datetime
from django.utils import timezone

@login_required(login_url='login')
def orders(request):
    customer_dict = {}
    orders = Orders.objects.all()
    customers = Customer.objects.all()
    for customer in customers:
        customer_dict[customer.id] = customer.title
    context = {'orders': orders, 'customer_dict': customer_dict}
    return render(request, 'orders/orders.html', context)

@login_required(login_url='login')
def single_order(request, pk):
    order = Orders.objects.get(id=pk)
    context = {'order': order}
    return render(request, 'orders/single_order.html', context)

@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form}
    return render(request, 'orders/order_form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders')
    context = {'order': order}
    return render(request, 'orders/delete_template.html', context)

class OpenOrdersListView(View):

    def __init__(self, *args, **kwargs):
        super(OpenOrdersListView, self).__init__(*args, **kwargs)
        self.initial_date = timezone.now()

    def group_orders_by_week_day(self):
        weeks_quantity = 4
        week_number = 1
        up_date = self.initial_date# + datetime.timedelta(days=1)
        down_date = self.initial_date - datetime.timedelta(days=1)
        weekly_orders = []
        while week_number <= weeks_quantity:
            day = 1
            current_week_orders = []
            while day <= 7:
                date = up_date# - datetime.timedelta(days=1)
                customers = ''
                orders_sum = 0
                day_orders = Orders.objects.filter(created__range=[down_date, up_date])
                if len(day_orders) != 0:
                    for order in day_orders:
                        customers = customers + str(order.customer) + ';'
                        orders_sum += order.amount
                    current_week_orders.append({'date': date, 'customers': customers, 'orders_sum': orders_sum})
                day += 1
                up_date = down_date# + datetime.timedelta(days=1)
                down_date = down_date - datetime.timedelta(days=1)
            weekly_orders.append(current_week_orders)
            week_number += 1
        return weekly_orders


    def get(self, request):
        weekly_orders = self.group_orders_by_week_day()
        current_week_orders = weekly_orders[0]

        context = {'current_week_orders': current_week_orders}
        return render(request, "orders/open_orders_template.html", context)

    def post(self, request):
        current_week = request.POST['current_week']
        weekly_orders = self.group_orders_by_week_day()
        current_week_orders = weekly_orders[int(current_week)]

        context = {'current_week_orders': current_week_orders}
        return render(request, "orders/open_orders_template.html", context)


