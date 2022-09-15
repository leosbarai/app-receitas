from backend.views import *
from backend.serializers import RecipeSerializer
from backend.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    """Exibindo as Receitas"""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
