from backend.views import *
from backend.serializers import RecipeSerializer
from backend.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    """Exibindo as Receitas"""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['recipe']
    search_fields = ['recipe']
    filterset_fields = ['active']

    def create(self, request):
        response = location(self, request)
        return response
