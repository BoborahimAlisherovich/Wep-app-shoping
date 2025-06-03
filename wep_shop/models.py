from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class ReklamaImage(models.Model):
    image = models.ImageField(upload_to='Images/reklama/')



class User(models.Model):
    full_name = models.CharField(max_length=150)
    phone_numper = models.CharField(max_length=13,unique=True)
    email = models.EmailField()
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"


class Category(models.Model):
    image = models.ImageField(upload_to='Images/category/')
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/product/')
    slug = models.SlugField()
    price = models.IntegerField()
    description = models.TextField()
    quantity_stock = models.IntegerField(default=0, verbose_name="Ombordagi soni")
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-created_at']

    def clean(self):
        if self.total_price < 0:
            raise ValidationError("Total price cannot be negative.")

    def __str__(self):
        return f"Order {self.id} by {self.customer}"

class OrderItem(models.Model):
    pass

class Cart(models.Model):
    pass

class Delevery(models.Model):
    pass

class Address(models.Model):
    pass
