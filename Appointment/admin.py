from django.contrib import admin
from Appointment.models import Appointment



# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # form_class = CustomUserCreationForm
    list_display=['id','user','date','starttime','endtime','doctor','is_verified']
    list_display_links=['id','user','date']
    ordering = ['-date']
