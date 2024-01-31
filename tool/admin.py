from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

admin.site.register(Category, CategoryModelAdmin)


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'minimum_order', 'quantity']


admin.site.register(Product, ProductModelAdmin)
