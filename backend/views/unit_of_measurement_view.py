from backend.views import *
from backend.serializers import UnitOfMeasurementSerializer
from backend.models import UnitOfMeasurement


class UnitOfMeasurementViewSet(viewsets.ModelViewSet):
    """Exibindo Unidades de Medida"""
    queryset = UnitOfMeasurement.objects.all()
    serializer_class = UnitOfMeasurementSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['unit_of_measurement']
    search_fields = ['unit_of_measurement']
    filterset_fields = ['active']
