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
    path('trip_request/',views.trip_request,name='ad_tripreq'),
    path('vehicles/', views.ad_vehicle, name='admin_vehicles'),
    path('admin/vehicles/add/', views.admin_add_vehicle, name='admin_add_vehicle'),
    path('admin-dashboard/rentals/', views.admin_rental_requests_view, name='admin_rental_requests'),
    path('rental-requests/<int:id>/', views.admin_rental_detail, name='admin_rental_detail'),
    path('ad_index/', views.ad_index, name='ad_index'),
    path('admin/index/edit-image/<int:id>/', views.edit_index_image, name='edit_index_image'),
    path('admin/rental/specs/<int:id>/', views.admin_rental_specs, name='admin_rental_specs'),




]