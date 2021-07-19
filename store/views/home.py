from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category
from django.views import View

# Create your views here.

class Home(View):
    def post(self,request):
        product=request.POST.get('product')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print(product)
        print(cart)
        return redirect('/')
   
    def get(self,request):
        print('your email : ',request.session.get('email'))
        print('your id: ',request.session.get(id))
        products = None
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_all_product_by_id(category_id)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'index.html', data)

   