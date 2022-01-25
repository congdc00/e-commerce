from django.contrib.auth import get_user_model
User = get_user_model()

from django import forms

class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)
