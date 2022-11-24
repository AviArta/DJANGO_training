
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


class SensorsListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer