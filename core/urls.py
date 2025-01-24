from django.urls import path
from .views import parish_list, parish_add, parish_edit, parish_delete

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clergy/', views.clergy_list, name='clergy_list'),
    path('parishes/', views.parishes_list, name='parishes_list'),
    #path('appointments/', views.appointments_list, name='appointments_list'),
    path('appointments/', views.list_appointments, name='appointments_list'),
    path('events/', views.events_list, name='events_list'),
    path('clergy/add/', views.clergy_add, name='clergy_add'),
    path('clergy/edit/<int:pk>/', views.clergy_edit, name='clergy_edit'),
    path('clergy/delete/<int:pk>/', views.clergy_delete, name='clergy_delete'),
    path('parishes/', parish_list, name='parish_list'),
    path('parishes/add/', parish_add, name='parish_add'),
    path('parishes/edit/<int:parish_id>/', parish_edit, name='parish_edit'),
    path('parishes/delete/<int:parish_id>/', parish_delete, name='parish_delete'),
    
    # path('appointments/', views.list_appointments, name='list_appointments'),
    # path('appointments/create/', views.create_appointment, name='create_appointment'),
    # path('appointments/update/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    # path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointments/update/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),

    # path('events/', views.list_events, name='list_event'),
    # path('events/add/', views.add_event, name='add_event'),
    # path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    # path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),

   path('events/', views.list_events, name='events_list'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),

]


