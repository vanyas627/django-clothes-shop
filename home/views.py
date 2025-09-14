from django.shortcuts import render
from products.models import Brand
from .models import Peculiarities, AboutUs, Services
from products.models import Products,CategoriesProduct,Images
def home_view(request):
    peculiarities = Peculiarities.objects.filter(is_visible=True)
    featured_product = Products.objects.filter(is_visible=True, is_featured=True)
    category = CategoriesProduct.objects.filter(is_category_month=True, is_visible=True)
    categories = []
    for item in category:
        photo = Images.objects.filter(product__category=item, is_visible=True).first()
        categories.append({'category': item, 'photo': photo})
    return render(request, 'index.html',context={'product': featured_product,
                                                 'peculiarities':peculiarities,
                                                 'categories': categories})

def about_view(request):
    about = AboutUs.objects.get()
    services = Services.objects.all()
    brands = Brand.objects.all()
    return render(request,'about.html', context={'about': about,
                                                 'services': services,
                                                 'brand': brands})