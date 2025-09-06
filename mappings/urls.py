
from django.urls import path
from .views import MappingListCreateView, MappingForPatientView, MappingDetailView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mappings-list-create'),
    path('<int:patient_id>/', MappingForPatientView.as_view(), name='mappings-for-patient'),
    path('remove/<int:pk>/', MappingDetailView.as_view(), name='mappings-remove'),
]
