from django.db import models

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
    pass

class OrderItem(models.Model):
    pass

class Cart(models.Model):
    pass

class Delevery(models.Model):
    pass

class Adres(models.Model):
    pass