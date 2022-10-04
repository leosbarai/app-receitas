from backend.views import *
from backend.models import Category
from backend.serializers import CategorySerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """Exibindo as Categorias"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['category']
    search_fields = ['category']
    filterset_fields = ['active']

    def create(self, request):
        response = location(self, request)
        return response
