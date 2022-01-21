from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm
from .models import Product, Comment
from django.views.generic import ListView, DetailView

# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'pages/home.html'
    context_object_name = 'Products'
    paginate_by = 30
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

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, product=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "pages/product.html", {"product": product, "form": form})
