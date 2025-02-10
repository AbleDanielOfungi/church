from django.shortcuts import render
from .models import Clergy, Parish, Appointment, Event

def home(request):
    return render(request, 'core/home.html')

def clergy_list(request):
    clergy = Clergy.objects.all()
    return render(request, 'core/clergy_list.html', {'clergy': clergy})

def parishes_list(request):
    parishes = Parish.objects.all()
    return render(request, 'parishes/parish_list.html', {'parishes': parishes})

def appointments_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'core/appointments_list.html', {'appointments': appointments})

def events_list(request):
    events = Event.objects.all()
    return render(request, 'core/events_list.html', {'events': events})



# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clergy
from .forms import ClergyForm

# List all clergy
def clergy_list(request):
    clergy_list = Clergy.objects.all()
    return render(request, 'core/clergy_list.html', {'clergy_list': clergy_list})

# Add new clergy
def clergy_add(request):
    if request.method == 'POST':
        form = ClergyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clergy_list')
    else:
        form = ClergyForm()
    return render(request, 'core/clergy_form.html', {'form': form})

# Edit clergy
def clergy_edit(request, pk):
    clergy = get_object_or_404(Clergy, pk=pk)
    if request.method == 'POST':
        form = ClergyForm(request.POST, request.FILES, instance=clergy)
        if form.is_valid():
            form.save()
            return redirect('clergy_list')
    else:
        form = ClergyForm(instance=clergy)
    return render(request, 'core/clergy_form.html', {'form': form})

# Delete clergy
def clergy_delete(request, pk):
    clergy = get_object_or_404(Clergy, pk=pk)
    if request.method == 'POST':
        clergy.delete()
        return redirect('clergy_list')
    return render(request, 'core/clergy_confirm_delete.html', {'clergy': clergy})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Parish
from .forms import ParishForm

# List of Parishes
def parish_list(request):
    parishes = Parish.objects.all()
    return render(request, 'parishes/parish_list.html', {'parishes': parishes})

# Add a New Parish
def parish_add(request):
    if request.method == 'POST':
        form = ParishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parish_list')
    else:
        form = ParishForm()
    return render(request, 'parishes/parish_form.html', {'form': form})

# Edit Parish
def parish_edit(request, parish_id):
    parish = get_object_or_404(Parish, pk=parish_id)
    if request.method == 'POST':
        form = ParishForm(request.POST, instance=parish)
        if form.is_valid():
            form.save()
            return redirect('parish_list')
    else:
        form = ParishForm(instance=parish)
    return render(request, 'parishes/parish_form.html', {'form': form})

# Delete Parish
def parish_delete(request, parish_id):
    parish = get_object_or_404(Parish, pk=parish_id)
    if request.method == 'POST':
        parish.delete()
        return redirect('parish_list')
    return render(request, 'parishes/parish_confirm_delete.html', {'parish': parish})


from django.shortcuts import render
from .models import Appointment


def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'core/appointments/list.html', {'appointments': appointments})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment
from .forms import AppointmentForm  # You may need to create a form for this

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('list_appointments') 
    else:
        form = AppointmentForm(instance=appointment)
    
    return render(request, 'core/appointments/update.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment

def delete_appointment(request, appointment_id):
    # Get the appointment object
    appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
    
    # Delete the appointment
    appointment.delete()
    
    # Redirect back to the appointments list
    return redirect('list_appointments')

from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_appointments')  # Redirect back to the list page after saving
    else:
        form = AppointmentForm()
    
    return render(request, 'core/appointments/add.html', {'form': form})




#event views
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

# List Events
from django.shortcuts import render
from core.models import Event  # Import your Event model

def list_events(request):
    events = Event.objects.all()
    return render(request, 'core/events/list.html', {'events': events})

# Add Event
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_events')
    else:
        form = EventForm()
    return render(request, 'core/events/add.html', {'form': form})

# Update Event
def update_event(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('list_events')
    else:
        form = EventForm(instance=event)
    return render(request, 'core/events/edit.html', {'form': form, 'event': event})

# Delete Event
def delete_event(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    event.delete()
    return redirect('list_events')



#mass scheduling
from django.shortcuts import render, get_object_or_404, redirect
from .models import MassSchedule
from .forms import MassScheduleForm
from django.contrib import messages

def list_masses(request):
    masses = MassSchedule.objects.all()
    return render(request, 'core/mass_schedule/list.html', {'masses': masses})


def add_mass(request):
    if request.method == 'POST':
        form = MassScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mass scheduled successfully.")
            return redirect('list_masses')
    else:
        form = MassScheduleForm()
    return render(request, 'core/mass_schedule/form.html', {'form': form})


def edit_mass(request, schedule_id):
    mass = get_object_or_404(MassSchedule, schedule_id=schedule_id)
    if request.method == 'POST':
        form = MassScheduleForm(request.POST, instance=mass)
        if form.is_valid():
            form.save()
            messages.success(request, "Mass schedule updated successfully.")
            return redirect('list_masses')
    else:
        form = MassScheduleForm(instance=mass)
    return render(request, 'core/mass_schedule/form.html', {'form': form})

def delete_mass(request, schedule_id):
    mass = get_object_or_404(MassSchedule, schedule_id=schedule_id)
    mass.delete()
    messages.success(request, "Mass schedule deleted successfully.")
    return redirect('list_masses')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Sacrament
from .forms import SacramentForm
from django.contrib import messages

def list_sacraments(request):
    sacraments = Sacrament.objects.all()
    return render(request, 'core/sacrament/list.html', {'sacraments': sacraments})


def add_sacrament(request):
    if request.method == 'POST':
        form = SacramentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sacrament added successfully!")
            return redirect('list_sacraments')
    else:
        form = SacramentForm()
    return render(request, 'core/sacrament/add.html', {'form': form})


def edit_sacrament(request, sacrament_id):
    sacrament = get_object_or_404(Sacrament, pk=sacrament_id)
    if request.method == 'POST':
        form = SacramentForm(request.POST, instance=sacrament)
        if form.is_valid():
            form.save()
            messages.success(request, "Sacrament updated successfully!")
            return redirect('list_sacraments')
    else:
        form = SacramentForm(instance=sacrament)
    return render(request, 'core/sacrament/edit.html', {'form': form, 'sacrament': sacrament})


def delete_sacrament(request, sacrament_id):
    sacrament = get_object_or_404(Sacrament, pk=sacrament_id)
    if request.method == 'POST':
        sacrament.delete()
        messages.success(request, "Sacrament deleted successfully!")
        return redirect('list_sacraments')
    return render(request, 'core/sacrament/confirm_delete.html', {'sacrament': sacrament})

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Meeting
from .forms import MeetingForm

def list_meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'core/meeting/list.html', {'meetings': meetings})

def add_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Meeting added successfully!')
            return redirect('list_meetings')
    else:
        form = MeetingForm()
    return render(request, 'core/meeting/add.html', {'form': form})

def edit_meeting(request, pk):
    meeting = Meeting.objects.get(pk=pk)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Meeting updated successfully!')
            return redirect('list_meetings')
    else:
        form = MeetingForm(instance=meeting)
    return render(request, 'core/meeting/edit.html', {'form': form, 'meeting': meeting})

def delete_meeting(request, pk):
    meeting = Meeting.objects.get(pk=pk)
    meeting.delete()
    messages.success(request, 'Meeting deleted successfully!')
    return redirect('list_meetings')



from django.shortcuts import render, redirect
from .models import Role
from .forms import RoleForm  # You'll need to create this form for adding/editing roles

# List all roles
def list_roles(request):
    roles = Role.objects.all()
    return render(request, 'roles/list.html', {'roles': roles})

# Add new role
def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_roles')
    else:
        form = RoleForm()
    return render(request, 'roles/add.html', {'form': form})

# Edit an existing role
def edit_role(request, pk):
    role = Role.objects.get(pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('list_roles')
    else:
        form = RoleForm(instance=role)
    return render(request, 'roles/edit.html', {'form': form})

# Delete an existing role
def delete_role(request, pk):
    role = Role.objects.get(pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('list_roles')
    return render(request, 'roles/delete.html', {'role': role})
