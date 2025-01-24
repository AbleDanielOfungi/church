from django.contrib import admin
from .models import Clergy, Parish, Appointment, MassSchedule, Sacrament, Meeting, Role, Event, UserAccount, Announcement

admin.site.register(Clergy)
admin.site.register(Parish)
# admin.site.register(Appointment)
admin.site.register(MassSchedule)
admin.site.register(Sacrament)
admin.site.register(Meeting)
admin.site.register(Role)
admin.site.register(Event)
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