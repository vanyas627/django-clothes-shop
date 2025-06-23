from django.shortcuts import render
from .models import Peculiarities, About_Us, Services
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
    about = About_Us.objects.get()
    services = Services.objects.all()
    return render(request,'about.html', context={'about': about,
                                                 'services': services})