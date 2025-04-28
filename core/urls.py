from django.urls import path
from .views import (
    contact_view,about_view
)

urlpatterns = [
    path('contact-us/',contact_view,name='contact_us'),
    path('about-us/',about_view,name='about_us')
]