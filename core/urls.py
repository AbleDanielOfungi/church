from django.urls import path
from .views import parish_list, parish_add, parish_edit, parish_delete
from .views import list_masses, add_mass, edit_mass, delete_mass
from .views import list_sacraments, add_sacrament, edit_sacrament, delete_sacrament
from .views import list_sacraments, add_sacrament, edit_sacrament

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clergy/', views.clergy_list, name='clergy_list'),
    path('parishes/', views.parishes_list, name='parishes_list'),
    #path('appointments/', views.appointments_list, name='appointments_list'),
    path('appointments/', views.list_appointments, name='appointments_list'),
    

    path('events/', views.list_events, name='list_events'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    #path('events/', list_events, name='events_list'),
    path('events/', views.events_list, name='events_list'),
    path('clergy/add/', views.clergy_add, name='clergy_add'),
    path('clergy/edit/<int:pk>/', views.clergy_edit, name='clergy_edit'),
    path('clergy/delete/<int:pk>/', views.clergy_delete, name='clergy_delete'),
    path('parishes/', parish_list, name='parish_list'),
    path('parishes/add/', parish_add, name='parish_add'),
    path('parishes/edit/<int:parish_id>/', parish_edit, name='parish_edit'),
    path('parishes/delete/<int:parish_id>/', parish_delete, name='parish_delete'),
    
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointments/update/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    
    path('mass_schedules/', views.list_masses, name='list_masses'),
    path('mass_schedules/', views.list_masses, name='mass_list'),
    path('mass_schedules/add/', views.add_mass, name='add_mass'),
    path('mass_schedules/edit/<int:schedule_id>/', views.edit_mass, name='edit_mass'),
    path('mass_schedules/delete/<int:schedule_id>/', views.delete_mass, name='delete_mass'),

    path('sacraments/', list_sacraments, name='list_sacraments'),
    path('sacraments/add/', add_sacrament, name='add_sacrament'),
    path('sacraments/edit/<int:sacrament_id>/', edit_sacrament, name='edit_sacrament'),
    path('sacraments/delete/<int:sacrament_id>/', delete_sacrament, name='delete_sacrament'),


    path('meetings/', views.list_meetings, name='list_meetings'),
    path('meetings/add/', views.add_meeting, name='add_meeting'),
    path('meetings/edit/<int:pk>/', views.edit_meeting, name='edit_meeting'),
    path('meetings/delete/<int:pk>/', views.delete_meeting, name='delete_meeting'),


    path('roles/', views.list_roles, name='list_roles'),  # List all roles
    path('roles/add/', views.add_role, name='add_role'),  # Add new role
    path('roles/edit/<int:pk>/', views.edit_role, name='edit_role'),  # Edit an existing role
    path('roles/delete/<int:pk>/', views.delete_role, name='delete_role'),  # Delete a role



]


