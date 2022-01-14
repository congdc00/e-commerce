from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView, DetailView

# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'pages/home.html'
    context_object_name = 'Products'
    paginate_by = 1
"""class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product.html'"""
def contact(request):
    return render(request, 'pages/contact.html')
def product(request, id):
    product = Product.objects.get(id = id)
    Data = {'Product': product}
    return render(request, 'pages/product.html', Data)
def error(request):
    return render(request, 'pages/error.html')
