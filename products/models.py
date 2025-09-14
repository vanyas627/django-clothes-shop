from django.db import models


class CategoriesProduct(models.Model):

    title = models.CharField(max_length=50)
    is_visible = models.BooleanField(default=False)
    is_category_month = models.BooleanField(default=False)
    category = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='subcategories')
    slug = models.SlugField(unique=True,null=False, blank=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created']
        verbose_name = 'Category Products'
        verbose_name_plural = 'Categories Products'


class Brand(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    photo = models.ImageField(upload_to='brands/', null=True, blank=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title

class Color(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.name


class Products(models.Model):

    title = models.CharField(max_length=50, null=False, blank=False)
    is_visible = models.BooleanField(default=False)
    price = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    color = models.ManyToManyField(Color, related_name='products', blank=True)
    size = models.ManyToManyField(Size, related_name='products', blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    category = models.ManyToManyField(CategoriesProduct, related_name='products')
    slug = models.SlugField(unique=True, blank=False, null=False)
    photo = models.ImageField(upload_to='products/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField(default=0)
    comments = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'


    class Meta:
        ordering = ['-created']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Images(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    is_visible = models.BooleanField(default=False)
    featured_photo = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class Specification(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Specification'
        verbose_name_plural = 'Specifications'


