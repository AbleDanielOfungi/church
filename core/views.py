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



from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm


def list_events(request):
    events = Event.objects.all()  # Retrieve all events from the database
    print(events)  # Debugging line to check if events are fetched correctly
    return render(request, 'core/events/list.html', {'events': events})

# Add a new event
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()  # Save the event to the database
            return redirect('list_events')  # Redirect to the events list after saving
    else:
        form = EventForm()  # Create an empty form for GET request

    return render(request, 'core/events/add.html', {'form': form})

# Update an event
def update_event(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()  # Save the updated event to the database
            return redirect('list_events')  # Redirect to the events list after saving
    else:
        form = EventForm(instance=event)  # Pre-fill the form with the current event data

    return render(request, 'core/events/update.html', {'form': form})

# Delete an event
def delete_event(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    event.delete()  # Delete the event from the database
    return redirect('list_events')  # Redirect to the events list after deleting
