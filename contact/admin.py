from django.contrib import admin
from .models import Contact, Order, CartItem



@admin.register(CartItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'size','quantity', 'total', 'order')
    list_filter = ('order',)



class CartItemInLine(admin.TabularInline):

    model = CartItem
    extra = 0
    fields = ['product', 'size', 'price', 'quantity']

@admin.register(Order)
class CartAdmin(admin.ModelAdmin):

    list_display = ('fullname', 'email', 'phone', 'adress')
    inlines = [CartItemInLine]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject')

