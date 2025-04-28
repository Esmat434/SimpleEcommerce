from django import forms
from .models import Contact

class ContactCreatoinForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'})
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'})
    )
    subject = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Subject'})
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Message'})
    )
    class Meta:
        model = Contact
        fields = ['username','email','phone_number','subject','message']