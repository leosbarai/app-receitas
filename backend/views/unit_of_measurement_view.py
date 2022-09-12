from backend.views import *
from backend.serializers import UnitOfMeasurementSerializer
from backend.models import UnitOfMeasurement


class UnitOfMeasurementView(viewsets.ModelViewSet):
    """Exibindo Unidades de Medida"""
    queryset = UnitOfMeasurement.objects.all()
    serializer_class = UnitOfMeasurementSerializer
