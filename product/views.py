from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum,Avg
from .models import (
    Product,Tag,Review
)
# Create your views here.

def product_list(request):
    tags = Tag.objects.all()
    products = Product.objects.prefetch_related('productimage_set').order_by('-created_at')
    if request.method == 'POST':
        data = request.POST
        btn = data.get('tag_btn')

        if btn != 'Product All':
            products = Product.objects.prefetch_related('productimage_set').filter(tag__name = btn).order_by('-created_at')
    return render(request,'product_list.html',{'products':products,'tags':tags})

def product_detail(request,slug):
    product = get_object_or_404(Product.objects.prefetch_related('productimage_set'),slug = slug)
    rate = product.review_set.aggregate(total = Sum('rating'))
    return render(request,'product_detail.html',{'product':product,'rate':rate})

def rate_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            product_id = data.get('product_id')
            rate = data.get('rate')
    
            product = get_object_or_404(Product,id = product_id)
            review = Review.objects.update_or_create(
                product = product,
                user = request.user,
                defaults={'rate':rate}
            )
            rate = Review.objects.aggregate(new_avg = Avg('rating'))
            return JsonResponse({'new_average':rate['new_avg']},status = 200)
    return JsonResponse({'error:':'This is error.'})