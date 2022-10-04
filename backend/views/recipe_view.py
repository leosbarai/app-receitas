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
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
