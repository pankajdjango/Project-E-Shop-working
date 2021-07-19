from store.models import Customer
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.views import View


# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        error_message = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_By_Email(email)
        if customer:
            match_Password = check_password(password, customer.password)
            if match_Password:
                request.session['id']=customer.id
                request.session['email']=customer.email
                return redirect('/')
            else:
                error_message = 'Email or Password Invailed !'
        else:
            error_message = 'Email or Password Invailed !'
        return render(request, 'login.html', {'error': error_message})
