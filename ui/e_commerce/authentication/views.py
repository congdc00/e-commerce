from django.http import HttpResponseRedirect
from django.shortcuts import render
from.forms import RegistrationForm
# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    Data = {'form': form}
    return render(request, 'register.html', Data)
