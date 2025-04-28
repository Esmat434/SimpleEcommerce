from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from .forms import UserCreationForm
from .decorators import (
    login_required,logout_required
)
# Create your views here.

@logout_required
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request,'signup.html',{'form':form})
    form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

@logout_required
def login_user(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username = username, password = password)

        if user:
            login(request,user)
            return redirect('product_list')
        return render(request,'login.html',{'error_message':'Username or Password is invalid.'})
    return render(request,'login.html')

@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('product_list')
    return render(request,'logout.html')

@login_required
def profile(request):
    return render(request,'profile.html',{'user':request.user})