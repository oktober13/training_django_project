from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerializer


# Create your views here.
def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer
