from django.contrib import admin
from .models import (
    Category,Tag,Brand,Product,ProductImage,Review
)
from .actions import (
    set_category_actions,set_tag_actions,set_brand_actions
)
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','tag','brand','slug','created_at']
    list_filter = ['name','category','tag','brand']
    search_fields = ['name','category']

    actions = [
        set_category_actions(1,'Mobile'),
        set_tag_actions(1,'Popular'),
        set_brand_actions(1,'Apple')
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','is_enable']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name','is_enable']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','is_enable']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product','created_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product','user','rating','created_at']