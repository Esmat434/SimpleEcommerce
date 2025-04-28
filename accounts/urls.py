from django.urls import path
from .views import (
    signup,login_user,logout_user,profile
)

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('profile/',profile,name='profile'),
]