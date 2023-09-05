from django.contrib.auth import views
from django.urls import path
from .views.index import home, signup, account, edit_account
from .views.product import shop, product

urlpatterns = [
    path("", home, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='product/login.html'), name='login'),\
    path('shop/', shop, name='shop'),
    path('product/<slug:slug>/', product, name='product'),
    path('account/', account, name='account'),
    path('edit_account/', edit_account, name='edit_account'),
]