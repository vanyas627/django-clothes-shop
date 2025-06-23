"""
URL configuration for My_clothes_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from home.views import home_view,about_view
from django.conf import settings
from django.conf.urls.static import static
from products.views import products_in_category_view,product_view
from contact.views import contact_view, cart_view, delete_item_in_cart, checkout_view, history_orders_views
from users.views import register_view, login_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('users/', include('users.urls')),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('category/', products_in_category_view, name='category'),
    path('order/', cart_view, name='order'),
    path('order/checkout/', checkout_view, name='checkout'),
    path('order/delete/<int:item_id>/', delete_item_in_cart, name='delete_product'),
    path('category/<slug:slug>/', products_in_category_view, name='category_products'),
    path('product/<slug:slug>', product_view, name='product'),
    path('history/', history_orders_views, name='history')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)