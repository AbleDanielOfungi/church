from django.contrib import admin
from .models import Clergy, Parish, Appointment, MassSchedule, Sacrament, Meeting, Role, Event, UserAccount, Announcement

admin.site.register(Clergy)
admin.site.register(Parish)
# admin.site.register(Appointment)
#admin.site.register(MassSchedule)
# admin.site.register(Sacrament)
admin.site.register(Meeting)
admin.site.register(Role)
# admin.site.register(Event)
admin.site.register(UserAccount)
admin.site.register(Announcement)



# from django.contrib import admin
# from .models import Appointment

# @admin.register(Appointment)
# class AppointmentsAdmin(admin.ModelAdmin):
#     list_display = ('appointment_type', 'appointment_date', 'appointment_time', 'priest', 'venue')
#     list_filter = ('appointment_date', 'appointment_type')
#     search_fields = ('appointment_type', 'venue', 'description')

from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_type', 'appointment_date', 'appointment_time', 'priest', 'venue')
    list_filter = ('appointment_date', 'appointment_type')
    search_fields = ('appointment_type', 'venue', 'description')


#event
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'event_time', 'event_venue', 'organizer')
    search_fields = ('event_name', 'event_venue', 'organizer__first_name', 'organizer__last_name')
    list_filter = ('event_date', 'organizer')
   

from django.contrib import admin
from .models import MassSchedule  # Import the MassSchedule model

# Register the MassSchedule model in the admin interface
@admin.register(MassSchedule)
class MassScheduleAdmin(admin.ModelAdmin):
    list_display = ('schedule_id', 'parish', 'mass_time', 'mass_date', 'priest', 'description', 'timestamp')  # Fields to display in the list view
    list_filter = ('parish', 'mass_date', 'priest')  # Filter options in the admin
    search_fields = ('parish__parish_name', 'priest__first_name', 'priest__last_name')  # Searchable fields
    ordering = ('mass_date', 'mass_time')  # Default ordering for mass schedules


from django.contrib import admin
from .models import Sacrament

@admin.register(Sacrament)
class SacramentAdmin(admin.ModelAdmin):
    list_display = ('sacrament_type', 'recipient_name', 'priest', 'sacrament_date', 'sacrament_location')
    search_fields = ('sacrament_type', 'recipient_name')



