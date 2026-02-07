from django.db import models

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)

    class Meta:
        db_table = 'patient_details'

    def __str__(self):
        return self.patient_name


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=20)

    class Meta:
        db_table = 'doctor_details'

    def __str__(self):
        return self.doctor_name


class Appointment(models.Model):
    appt_id = models.AutoField(primary_key=True)
    appt_date = models.DateField()
    appt_time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room_no = models.IntegerField()
    bldg_no = models.IntegerField()

    class Meta:
        db_table = 'appointment_details'

    def __str__(self):
        return f"Appointment {self.appt_id} - {self.patient.patient_name} with Dr. {self.doctor.doctor_name}"