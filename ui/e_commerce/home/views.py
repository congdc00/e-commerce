from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

from authentication.forms import CommentForm
from product.models import Product
from authentication.models import Comment
from django.views.generic import ListView, DetailView

# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'pages/home.html'
    context_object_name = 'Products'
    paginate_by = 4
"""class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/home.html'"""
def contact(request):
    return render(request, 'pages/contact.html')
"""def home(request, id):
    home = Product.objects.get(id = id)
    Data = {'Product': home}
    return render(request, 'pages/home.html', Data)"""
def error(request):
    return render(request, 'pages/error.html')

