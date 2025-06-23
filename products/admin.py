from django.contrib import admin

from .models import Products,CategoriesProduct,Images,Specification, Brand, Color, Size


admin.site.register(CategoriesProduct)
admin.site.register(Images)
admin.site.register(Specification)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price']
    list_display_links = ['title', 'brand']
    list_filter = ['is_visible', 'is_featured', 'created', 'brand', 'category']
    list_editable = ['price']
    prepopulated_fields = {"slug": ("title",)}