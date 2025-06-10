from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashbard'),
    path('services/',views.services,name='service'),
    path('services/add/', views.add_service, name='add_service'),
    path('services/section/edit/', views.edit_services_section, name='edit_services_section'),
    path('services/edit/<int:id>/', views.edit_service_offered, name='edit_service_offered'),
    path('services/delete/<int:id>/', views.delete_service, name='delete_service'),
    path('ad_about/', views.ad_about, name='ad_about'),
    path('ad_viewabout/', views.about_view, name='ad_viewabout'),


]