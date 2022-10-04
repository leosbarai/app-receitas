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
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
