from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
# Create your views here.
from product.models import Product, Category
from .models import Order
from . import forms
from cart.models import Cart
from django.contrib.auth import get_user_model
User = get_user_model()

def order(request):
    category = Category.objects.all()
    total=0;
    carts=request.session['cart']
    for key, value in carts.items ():
        total +=int(value['price'])*int(value['num'])
    data = {'category': category, 'total': total}
    return render(request, 'order.html',data)

