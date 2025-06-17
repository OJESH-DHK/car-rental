from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('car/', views.car, name='car'),
    path('car/<str:car_type>/<int:id>/', views.car_single, name='car_single'),

    path('contact/', views.contact, name='contact'),
    path('main/', views.main, name='main'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='servicess'),
    path('book/<int:vehicle_id>/', views.book_vehicle, name='book_vehicle'),
    path('put_car_on_rent/', views.put_car_on_rent, name='put_car_on_rent'),
    path('rent-success/', views.rent_success, name='rent_success'),
    path('book/user-car/<int:id>/', views.book_user_vehicle, name='book_user_vehicle'),
    
]