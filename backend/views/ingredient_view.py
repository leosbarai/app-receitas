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
