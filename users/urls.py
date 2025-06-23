from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import register_view,login_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html',
                                                                   success_url= reverse_lazy('change-password-done')), name='change-password'),
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html',),
         name='change-password-done')
]