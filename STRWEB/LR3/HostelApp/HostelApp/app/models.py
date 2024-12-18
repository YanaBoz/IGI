from os import name
from turtle import teleport
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employee = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
        
class News(models.Model):
    title = models.TextField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)

class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    need = models.TextField()

class Contact(models.Model):
    description = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')

class About(models.Model):
    description = models.TextField()
    video = models.FileField(upload_to='VidosEki/')
    image = models.ImageField(upload_to='images/')
    history= models.TextField()
    details = models.TextField()
    certificate = models.ImageField(upload_to='images/')

class MainMod(models.Model):
    image = models.ImageField(upload_to='images/')
    advertising = models.ImageField(upload_to='images/')
    partner = models.TextField()
    part_image = models.ImageField(upload_to='images/')
    link = models.TextField()
    
class Service(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

class CartItem(models.Model):
    product = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Cart(models.Model):
    user = models.ManyToManyField(User)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.quantity * item.product.price
        return total

class Employee(models.Model):
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    phone = models.TextField() 
    email = models.TextField() 

class Full_News(models.Model):
    news = models.OneToOneField(News, on_delete=models.CASCADE)
    text = models.TextField()

class Answer(models.Model):
    name = models.TextField()
    text = models.TextField()

class PolCon(models.Model):
    text = models.TextField()

class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField()

class Review2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField()

class Cart_2(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       created_at = models.DateTimeField(auto_now_add=True)

class CartItem_2(models.Model):
       cart = models.ForeignKey(Cart_2, on_delete=models.CASCADE)
       product = models.ForeignKey(Service, on_delete=models.CASCADE)
       quantity = models.PositiveIntegerField(default=1)

       def __str__(self):
           return f"{self.product.name} x {self.quantity}"

class Order(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       created_at = models.DateTimeField(auto_now_add=True)
       total_price = models.DecimalField(max_digits=10, decimal_places=2)

class OrderItem(models.Model):
       order = models.ForeignKey(Order, on_delete=models.CASCADE)
       product = models.ForeignKey(Service, on_delete=models.CASCADE)
       quantity = models.PositiveIntegerField(default=1)
       price = models.DecimalField(max_digits=10, decimal_places=2)

class Session(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DateTimeField()