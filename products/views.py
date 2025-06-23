from django.shortcuts import render,get_object_or_404
from .models import CategoriesProduct,Products,Specification,Images, Brand, Color, Size


def products_in_category_view(request,slug=None):

    categories = CategoriesProduct.objects.filter(category__isnull=True, is_visible=True)
    brands = Brand.objects.all()
    colors = Color.objects.all()
    sizes = Size.objects.all()

    if slug:
        category = get_object_or_404(CategoriesProduct, slug=slug)
        products = Products.objects.filter(category=category, is_visible=True)
    else:
        products = Products.objects.filter(is_visible=True)

    brand = request.GET.get('brand')
    if brand:
        products = products.filter(brand__title__iexact=brand)

    color = request.GET.get('color')
    if color:
        products = products.filter(color__name__iexact=color)

    size = request.GET.get('size')
    if size:
        products = products.filter(size__name__iexact=size)


    sort_option = request.GET.get('sort')

    if sort_option == 'title_asc':
        products = products.order_by('title')
    elif sort_option == 'title_desc':
        products = products.order_by('-title')
    elif sort_option == 'price_asc':
        products = products.order_by('price')
    elif sort_option == 'price_desc':
        products = products.order_by('-price')


    return render(request, 'shop.html', context={
        'products': products,
        'categories': categories,
        'brands': brands,
        'colors': colors,
        'sizes': sizes,
    })
def product_view(request,slug=None):
    specification = Specification.objects.filter(is_visible=True)
    product = Products.objects.get(slug=slug)
    images = Images.objects.filter(is_visible=True, featured_photo=False, product=product)
    related_products = Products.objects.filter(is_visible=True,category__in=product.category.all()
    ).exclude(id=product.id)
    return render(request, 'shop-single.html', context={'product': product,
                                                        'photo': images,
                                                        'specification': specification,
                                                        'related_products': related_products,
                                                        'range_yellow_stars': range(product.rating),
                                                        'range_grey_stars': range(5-product.rating)})
