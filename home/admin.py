from django.contrib import admin
from .models import Peculiarities, AboutUs, Services


@admin.register(Peculiarities)
class AdminPeculiarities(admin.ModelAdmin):
    list_display = ['title', 'is_visible', 'description1']
    list_filter = ['is_visible']
    list_editable = ['is_visible', 'description1']


@admin.register(Services)
class AdminServices(admin.ModelAdmin):
       list_display = ['service', 'service_sign']
       list_editable = ['service_sign']


admin.site.register(AboutUs)




