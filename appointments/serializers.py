from rest_framework import serializers
from .models import Patient, Doctor, Appointment


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['appt_id', 'doctor', 'patient', 'appt_date', 'appt_time', 'room_no', 'bldg_no']