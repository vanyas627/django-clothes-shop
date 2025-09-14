from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from .validators import phone_validators

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.email}'



class Order(models.Model):

    fullname = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, validators=[phone_validators])
    adress = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'Order {self.id} by {self.fullname}'



class CartItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)


    def total(self):
        return round(self.quantity * self.price,2)


    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    def __str__(self):
        return f'Name: {self.product.title} Qty: {self.quantity} Totsl: {self.total()}'
