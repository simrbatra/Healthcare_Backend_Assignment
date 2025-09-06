
from rest_framework import generics, permissions, status
from .models import Mapping
from .serializers import MappingSerializer
from rest_framework.response import Response

class MappingListCreateView(generics.ListCreateAPIView):
    queryset = Mapping.objects.all().order_by('-assigned_at')
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

class MappingForPatientView(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        return Mapping.objects.filter(patient_id=patient_id).order_by('-assigned_at')

class MappingDetailView(generics.DestroyAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
