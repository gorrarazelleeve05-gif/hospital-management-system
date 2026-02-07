from rest_framework import serializers
from .models import Patient, Doctor, Appointment


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['url', 'patient_id', 'patient_name', 'address', 'contact_no', 'age', 'sex']


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['url', 'doctor_id', 'doctor_name', 'specialization', 'sex', 'contact_no']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['url', 'appt_id', 'doctor', 'patient', 'appt_date', 'appt_time', 'room_no', 'bldg_no']