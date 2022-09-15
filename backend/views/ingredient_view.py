from backend.views import *
from backend.serializers import IngredientSerializer
from backend.models import Ingredient


class IngredientViewSet(viewsets.ModelViewSet):
    """Exibindo os Ingredientes"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
