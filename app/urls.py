from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('car/', views.car, name='car'),
    path('car-single/<int:id>/', views.car_single, name='car_single'),
    path('contact/', views.contact, name='contact'),
    path('main/', views.main, name='main'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
]