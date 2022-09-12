from backend.views import *
from backend.models import Category
from backend.serializers import CategorySerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """Exibindo as Categorias"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
