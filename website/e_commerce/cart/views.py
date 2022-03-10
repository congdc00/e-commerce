from django.shortcuts import render, get_object_or_404
from product.models import Category, Product
# Create your views here.



def cart(request):
    category = Category.objects.all()
    total=0;
    carts=request.session['cart']
    for key, value in carts.items ():
        total +=int(value['price'])*int(value['num'])
    data = {'category': category, 'total': total}
    return render (request,'cart.html',data)

def success(request):
    return render(request, 'success.html')

