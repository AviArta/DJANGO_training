from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet


from logistic.serializers import ProductSerializer, StockSerializer
from logistic.models import Product, Stock


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id',]
    search_fields = ['title',]
    ordering_fields = ['id',]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', ]
    # search_fields = ['positions__product__id', ]  # для последнего запроса основного задания.
    search_fields = ['positions__product__title']
    ordering_fields = ['id', ]
