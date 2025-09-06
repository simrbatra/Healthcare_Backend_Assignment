
from rest_framework import serializers
from .models import Mapping
from doctors.serializers import DoctorSerializer
from patients.serializers import PatientSerializer

class MappingSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    doctor_id = serializers.IntegerField(write_only=True)
    patient_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Mapping
        fields = ['id','patient','doctor','patient_id','doctor_id','assigned_at']

    def create(self, validated_data):
        patient_id = validated_data.pop('patient_id')
        doctor_id = validated_data.pop('doctor_id')
        from patients.models import Patient
        from doctors.models import Doctor
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            raise serializers.ValidationError({'patient_id':'Patient not found'})
        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            raise serializers.ValidationError({'doctor_id':'Doctor not found'})
        mapping, created = Mapping.objects.get_or_create(patient=patient, doctor=doctor, defaults={'assigned_by': self.context['request'].user})
        if not created:
            raise serializers.ValidationError('This mapping already exists')
        return mapping
