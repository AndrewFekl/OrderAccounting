from django.shortcuts import render

def orders(request):
    context = {}
    return render(request, 'orders/orders.html', context)

def single_order(request, pk):
    context = {}
    return render(request, 'orders/single_order.html', context)
