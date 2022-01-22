
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
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
