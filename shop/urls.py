from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contactus'),
    path('tracker', views.tracker,name='tracker'),
    path('search', views.search,name='search'),
    path('productview/<int:myid>', views.productview,name='productview'),
    path('checkout', views.checkout,name='checkout'),
    path('cart', views.cart, name='cart'),
]
