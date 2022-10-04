from backend.views import *
from backend.serializers import UnitOfMeasurementSerializer
from backend.models import UnitOfMeasurement


class UnitOfMeasurementViewSet(viewsets.ModelViewSet):
    """Exibindo Unidades de Medida"""
    queryset = UnitOfMeasurement.objects.all()
    serializer_class = UnitOfMeasurementSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['unit_of_measurement']
    search_fields = ['unit_of_measurement']
    filterset_fields = ['active']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
