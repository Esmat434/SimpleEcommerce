from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True
    )
    is_enable = models.BooleanField(
        default=True
    )

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class Category(BaseModel):
    ...

class Tag(BaseModel):
    ...

class Brand(BaseModel):
    ...

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1048,blank=True)
    price = models.IntegerField()
    stock = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    tag = models.ForeignKey(Tag,on_delete=models.SET_NULL,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='products/',blank=True)
    created_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i,i) for i in range(1,6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product','user')