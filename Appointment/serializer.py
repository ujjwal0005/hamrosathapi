from rest_framework import serializers
from Appointment.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Appointment
        fields = ('id','user','date','starttime','endtime','doctor','is_verified','is_cancelled')

