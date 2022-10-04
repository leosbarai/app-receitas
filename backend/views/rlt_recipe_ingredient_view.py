from backend.views import *
from backend.serializers import RltRecipeIngredientSerializer
from backend.models import RltRecipeIngredient


class RltRecipeIngredientViewSet(viewsets.ModelViewSet):
    """Exibindo o Relacionamento de Receita e Ingredientes"""
    queryset = RltRecipeIngredient.objects.all()
    serializer_class = RltRecipeIngredientSerializer

    def create(self, request):
        response = location(self, request)
        return response
