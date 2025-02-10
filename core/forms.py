# core/forms.py
from django import forms
from .models import Clergy
from .models import Parish

class ClergyForm(forms.ModelForm):
    class Meta:
        model = Clergy
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'date_of_ordination', 
            'parish_assigned', 'role', 'contact_number', 'email', 'address', 'photo'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_ordination': forms.DateInput(attrs={'type': 'date'}),
        }


class ParishForm(forms.ModelForm):
    class Meta:
        model = Parish
        fields = ['parish_name', 'parish_location', 'parish_priest', 'contact_number', 'address']
        widgets = {
            'parish_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parish_location': forms.TextInput(attrs={'class': 'form-control'}),
            'parish_priest': forms.Select(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# from django import forms
# from .models import Appointment

# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['appointment_type', 'appointment_date', 'appointment_time', 'priest', 'venue', 'description']
#         widgets = {
#             'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
#             'appointment_type': forms.TextInput(attrs={'class': 'form-control'}),
#             'venue': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'}),
#         }


from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_type', 'appointment_date', 'appointment_time', 'priest', 'venue', 'description']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_type', 'appointment_date', 'appointment_time', 'priest', 'venue', 'description']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }


#event form
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'event_time', 'event_venue', 'description', 'organizer']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'event_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'event_venue': forms.TextInput(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'organizer': forms.Select(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import MassSchedule

class MassScheduleForm(forms.ModelForm):
    class Meta:
        model = MassSchedule
        fields = ['parish', 'priest', 'mass_date', 'mass_time', 'description']
        widgets = {
            'mass_date': forms.DateInput(attrs={'type': 'date'}),
            'mass_time': forms.TimeInput(attrs={'type': 'time'}),
        }

from django import forms
from .models import Sacrament

class SacramentForm(forms.ModelForm):
    sacrament_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Sacrament
        fields = ['sacrament_type', 'recipient_name', 'priest', 'sacrament_date', 'sacrament_location']



# forms.py
from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['meeting_title', 'meeting_date', 'meeting_time', 'meeting_venue', 'attendees', 'agenda', 'minutes']
        widgets = {
            'meeting_date': forms.DateInput(attrs={'type': 'date'}),
            'meeting_time': forms.TimeInput(attrs={'type': 'time'}),
        }


# forms.py
from django import forms
from .models import Role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name', 'permissions']
