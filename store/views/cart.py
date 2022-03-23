from store.models import Customer
from django.shortcuts import redirect, render
from django.views import View
from store.models.product import Product
# Create your views here.

class Cart(View):
    def get(self, request):
        ids=request.session.get('cart').keys()
        products=Product.get_product_by_id(ids)
        print(products)
        return render(request, 'cart.html',{'products':products})

    def post(self,request):
        return render(request,'cart.html')
