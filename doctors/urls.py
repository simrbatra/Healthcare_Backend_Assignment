
from django.urls import path
from .views import DoctorListCreateView, DoctorDetailView

urlpatterns = [
    path('', DoctorListCreateView.as_view(), name='doctors-list-create'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctors-detail'),
]
