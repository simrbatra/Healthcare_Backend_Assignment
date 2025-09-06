
from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from django.contrib.auth.models import User

class Mapping(models.Model):
    patient = models.ForeignKey(Patient, related_name='mappings', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='mappings', on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, related_name='assigned_mappings', on_delete=models.SET_NULL, null=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient','doctor')

    def __str__(self):
        return f"Patient {self.patient_id} -> Doctor {self.doctor_id}"
