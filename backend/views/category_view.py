from backend.views import *
from backend.models import Category
from backend.serializers import CategorySerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """Exibindo as Categorias"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['category']
    search_fields = ['category']
    filterset_fields = ['active']
