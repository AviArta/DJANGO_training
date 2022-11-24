from django.urls import path

from measurement.views import SensorsListCreateView, SensorRetrieveUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensorslist/', SensorsListCreateView.as_view()),
    path('sensorchange/<int:pk>/', SensorRetrieveUpdateView.as_view()),
    path('measurementcreate/', MeasurementCreateView.as_view()),]
