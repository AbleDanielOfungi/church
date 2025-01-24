from django.db import models

# class Clergy(models.Model):
#     clergy_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     date_of_ordination = models.DateField()
#     parish_assigned = models.CharField(max_length=200)
#     role = models.CharField(max_length=50)
#     contact_number = models.CharField(max_length=15)
#     email = models.EmailField(unique=True)
#     address = models.TextField()
#     photo = models.ImageField(upload_to='clergy_photos/')
#     timestamp = models.DateTimeField(auto_now_add=True)


class Clergy(models.Model):
    clergy_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_ordination = models.DateField()
    parish_assigned = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    photo = models.ImageField(upload_to='clergy_photos/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"


# class Parish(models.Model):
#     parish_id = models.AutoField(primary_key=True)
#     parish_name = models.CharField(max_length=200)
#     parish_location = models.CharField(max_length=300)
#     parish_priest = models.ForeignKey(Clergy, on_delete=models.SET_NULL, null=True)
#     contact_number = models.CharField(max_length=15)
#     address = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

class Parish(models.Model):
    parish_id = models.AutoField(primary_key=True)
    parish_name = models.CharField(max_length=100)
    parish_location = models.CharField(max_length=100)
    parish_priest = models.ForeignKey(Clergy, on_delete=models.SET_NULL, null=True, blank=True)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.parish_name


# class Appointment(models.Model):
#     appointment_id = models.AutoField(primary_key=True)
#     appointment_type = models.CharField(max_length=100)
#     appointment_date = models.DateField()
#     appointment_time = models.TimeField()
#     priest = models.ForeignKey(Clergy, on_delete=models.CASCADE)
#     venue = models.CharField(max_length=300)
#     description = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    appointment_type = models.CharField(max_length=100)  # E.g., meeting, confirmation
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    priest = models.ForeignKey(Clergy, on_delete=models.CASCADE)
    venue = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.appointment_type} - {self.appointment_date} at {self.venue}"


class MassSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    mass_time = models.TimeField()
    mass_date = models.DateField()
    priest = models.ForeignKey(Clergy, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Sacrament(models.Model):
    sacrament_id = models.AutoField(primary_key=True)
    sacrament_type = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=200)
    priest = models.ForeignKey(Clergy, on_delete=models.CASCADE)
    sacrament_date = models.DateField()
    sacrament_location = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

class Meeting(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    meeting_title = models.CharField(max_length=200)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_venue = models.CharField(max_length=300)
    attendees = models.ManyToManyField(Clergy)
    agenda = models.TextField()
    minutes = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    permissions = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# class Event(models.Model):
#     event_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=200)
#     event_date = models.DateField()
#     event_time = models.TimeField()
#     event_venue = models.CharField(max_length=300)
#     description = models.TextField()
#     organizer = models.ForeignKey(Clergy, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
# Assuming you have the Clergy model already

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_venue = models.CharField(max_length=255)
    description = models.TextField()
    organizer = models.ForeignKey(Clergy, on_delete=models.CASCADE)  # Link to Clergy or Admin
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_name} - {self.event_date} at {self.event_venue}"


class UserAccount(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Use Django's authentication system
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    last_login = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Announcement(models.Model):
    announcement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
