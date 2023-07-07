from django.shortcuts import render

from orders.models import SalesOrder


# Create your views here.
def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})
