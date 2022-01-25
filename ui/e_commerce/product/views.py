
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

from authentication.forms import CommentForm
from product.models import Product

def product(request, pk):
    product=get_object_or_404(Product, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, product=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "product.html", {"product": product, "form": form})

cart = {}
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def addcart(request):
    if is_ajax(request=request):
      id = request.POST.get('id')
      num = request.POST.get('num')
      html= render_to_string('addcart.html')

    productDetail = Product.objects.get(id=id)
    if id in cart.keys():
      itemCart = {
         'name':productDetail.name,
         'price':productDetail.price,
         'image':str(productDetail.image),
         'num' :int(cart[id]['num'])+1
      }
    else:
        itemCart = {
         'name':productDetail.name,
         'price':productDetail.price,
         'image':str(productDetail.image),
         'num' : int(num)
        }

    cart[id] = itemCart
    request.session['cart']=cart
    cartInfo=request.session['cart']

    return HttpResponse(html, {'cart': cartInfo})
