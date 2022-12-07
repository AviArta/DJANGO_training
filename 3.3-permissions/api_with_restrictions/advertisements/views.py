from django.db.models import Q
from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly #IsAdminUserOrReadOnly, IsAdminOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'favorite_by']


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()  # exclude(status='DRAFT')
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]
    throttle_classes = [AnonRateThrottle]
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend]


    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_anonymous:
            qs = qs.filter(status__in=['OPEN', 'CLOSED'])
        else:
            qs = qs.filter(Q(status__in=['OPEN', 'CLOSED']) | Q(creator=self.request.user, status__in=['DRAFT']))

        return qs

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly(), IsAuthenticated(),]
        return []
