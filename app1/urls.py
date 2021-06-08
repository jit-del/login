from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from.forms import LoginForm
urlpatterns = [
    # path('', views.home),
    path('',views.home,name='home'),
    path('registration/', views.CustomerRegiistrationView.as_view(), name='customerregistration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
]