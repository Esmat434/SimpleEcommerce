from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user','username','email','phone_number','created_at']
    list_filter = ['user','username']
    search_fields = ['username']