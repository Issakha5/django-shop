from django.contrib import admin
from .models.category import Category
from .models.product import Product
from .models.review import Review

# Register your models her
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)