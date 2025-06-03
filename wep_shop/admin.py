from django.contrib import admin
from .models import ReklamaImage, User, Category, Product, Order, OrderItem, Cart, Delevery, Address


@admin.register(ReklamaImage)
class ReklamaImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    search_fields = ['id']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_numper', 'email']
    search_fields = ['full_name', 'phone_numper', 'email']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status', 'total_price']
    search_fields = ['custumer']
    list_filter = ['status']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity_stock']
    search_fields = ['name', 'category__name']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('name',)}