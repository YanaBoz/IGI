from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import CartItem_2, Cart_2

@receiver(post_save, sender=CartItem_2)
def update_cart_total(sender, instance, created, **kwargs):
    cart = instance.cart
    cart_items = CartItem_2.objects.filter(cart=cart)
    cart.total_price = sum(item.quantity * item.product.price for item in cart_items)
    cart.save()

@receiver(post_delete, sender=CartItem_2)
def update_cart_total_delete(sender, instance, **kwargs):
    cart = instance.cart
    cart_items = CartItem_2.objects.filter(cart=cart)
    cart.total_price = sum(item.quantity * item.product.price for item in cart_items)
    cart.save()
