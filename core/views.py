from django.shortcuts import render,redirect
from .forms import (
    ContactCreatoinForm
)
# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactCreatoinForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user if request.user.is_authenticated else None
            contact.save()
            return redirect('product_list')
        return render(request,'contact.html',{'form':form})
    form = ContactCreatoinForm()
    return render(request,'contact_us.html',{'form':form})

def about_view(request):
    return render(request,'about_us.html')