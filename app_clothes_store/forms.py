from .models import Cloth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Favorite


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ['username', 'email', 'password1', 'password2']


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField()
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].label = ""
