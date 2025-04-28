from django import forms
from .models import CustomUser

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName.'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email.'})
    )
    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Enter First Name.'}
        )
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Enter Last Name.'}
        )
    )
    phone_number = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Enter Phone Number.'}
        )
    )
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={'class':'form-control','placeholder':'Select Avatar.'}
        )
    )
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class':'form-control','placholder':'Enter BirthDate'})
    )
    password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(
            attrs={'class':'form-control','placeholder':'Enter Password.'}
        )
    )
    password2 = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(
            attrs={'class':'form-control','placeholder':'Enter Confirmation Password.'}
        )
    )
    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name','phone_number','avatar','birth_date','password','password2')
    
    def clea_username(self):
        username = self.cleaned_data['username']

        if CustomUser.objects.filter(username = username).exists():
            raise forms.ValidationError("This Username Already Exists.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']

        if CustomUser.objects.filter(email = email).exists():
            raise forms.ValidationError("This Eamil Already Exists.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if not password or not password2:
            raise forms.ValidationError("Your must set your password and confirmation password.")
        if len(password) < 8:
            raise forms.ValidationError("Your age must be at least 18+.")
        
        if password != password2:
            raise forms.ValidationError("Your password and confirm password must be same.")
        
        return cleaned_data
    
    def save(self, commit = ...):
        user = super().save(commit = False)
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user