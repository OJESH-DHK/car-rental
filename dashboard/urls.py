from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashbard'),
    path('services/',views.services,name='service'),
    path('services/add/', views.add_service, name='add_service'),
    path('services/section/edit/', views.edit_services_section, name='edit_services_section'),
    path('services/edit/<int:id>/', views.edit_service_offered, name='edit_service_offered'),
    path('services/delete/<int:id>/', views.delete_service, name='delete_service'),
    path('ad_about/', views.ad_about, name='ad_about'),
    path('ad_viewabout/', views.about_view, name='ad_viewabout'),
    path('trip_request/',views.trip_request,name='ad_tripreq'),
    path('vehicles/', views.ad_vehicle, name='admin_vehicles'),
    path('vehicles/delete/<int:id>/', views.delete_vehicle, name='delete_vehicle'),
    path('admin/vehicles/add/', views.admin_add_vehicle, name='admin_add_vehicle'),
    path('dashboard/vehicle/edit/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('admin-dashboard/rentals/', views.admin_rental_requests_view, name='admin_rental_requests'),
    path('rental-requests/<int:id>/', views.admin_rental_detail, name='admin_rental_detail'),
    path('admin/rentals/delete/<int:id>/', views.delete_rental_request, name='delete_rental_request'),
    path('admin/contact-details/', views.admin_contact_details, name='admin_contact_details'),
    path('admin/contact-detail/edit/', views.admin_contact_detail_edit, name='admin_contact_detail_edit'),
    path('admin/contact-messages/', views.admin_contact_messages, name='admin_contact_messages'),
    path('ad_index/', views.ad_index, name='ad_index'),
    path('admin/index/edit-image/<int:id>/', views.edit_index_image, name='edit_index_image'),
    path('admin/rental/specs/<int:id>/', views.admin_rental_specs, name='admin_rental_specs'),
    path('bookings/', views.booking_dashboard, name='booking_dashboard'),
    path('dashboard/bookings/delete-admin/<int:id>/', views.delete_admin_booking, name='delete_admin_booking'),
    path('dashboard/bookings/delete-user/<int:id>/', views.delete_user_booking, name='delete_user_booking'),
    path('admin/testimonials/', views.admin_testimonials, name='admin_testimonials'),
    path('admin/testimonials/edit/<int:pk>/', views.edit_testimonial, name='edit_testimonial'),
    path('admin/testimonials/delete/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
    path('admin/testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('dashboard/admin/counter/', views.admin_counter, name='admin_counter'),
    path('admin/blogs/', views.ad_viewblog, name='ad_viewblog'),
    path('admin/blogs/add/', views.ad_addblog, name='ad_addblog'),
    path('admin/blogs/edit/<int:blog_id>/', views.ad_editblog, name='ad_editblog'),
    path('admin/blogs/delete/<int:blog_id>/', views.ad_deleteblog, name='ad_deleteblog'),
    path('trip-requests/delete/<int:id>/', views.delete_trip_request, name='delete_trip_request'),
    path('contact-messages/delete/<int:id>/', views.delete_contact_message, name='delete_contact_message'),






]