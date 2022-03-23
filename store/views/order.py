from store.models import Customer
from django.shortcuts import redirect, render
from django.views import View
from store.models.product import Product
from store.models.orders import Orders


# Create your views here.

class Order_View(View):
    def get(self, request):
        customer = request.session.get('customer_id')
        print(customer)
        orders = Orders.get_orders_by_customer_id(customer)
        print("orders===",orders)
        return render(request,'orders.html',{'orders':orders})
