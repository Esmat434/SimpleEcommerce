from functools import wraps
from django.shortcuts import redirect

def login_required(view_func):
    @wraps(view_func)
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request,*args,**kwargs)
    return wrapper

def logout_required(view_func):
    @wraps(view_func)
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return view_func(request,*args,**kwargs)
    return wrapper