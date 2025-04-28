from django import forms
from .models import (
    ShippingAddress,Payment
)

class ShippingAddressCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'})
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'})
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'})
    )
    pone_number = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'})
    )
    address1 = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Address'})
    )
    address2 = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Second Address'})
    )
    country = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Country'})
    )
    city = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'})
    )
    zipcode = forms.CharField(
        max_length=6,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Zip Code'})
    )
    class Meta:
        model = ShippingAddress
        fields = (
            'first_name','last_name','username','email','phone_number','address1',
            'address2','country','city','zipcode'
        )

class PaymentCreationForm(forms.ModelForm):
    cart_number = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Cart Number'})
    )
    cart_holder = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Cart Holder'})
    )
    expiry_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class':'form-control'})
    )
    cvv = forms.CharField(
        max_length=4,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter CVV'})
    )
    class Meta:
        model = Payment
        fields = (
            'cart_number','cart_holder','expiry_date','cvv'
        )