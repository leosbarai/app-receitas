
from backend.views import *
from backend.serializers import IngredientSerializer
from backend.models import Ingredient


class IngredientViewSet(viewsets.ModelViewSet):
    """Exibindo os Ingredientes"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['ingredient']
    search_fields = ['ingredient']
    filterset_fields = ['active']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
