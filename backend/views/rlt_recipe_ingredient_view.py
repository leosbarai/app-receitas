from backend.views import *
from backend.serializers import RltRecipeIngredientSerializer
from backend.models import RltRecipeIngredient


class RltRecipeIngredientViewSet(viewsets.ModelViewSet):
    """Exibindo o Relacionamento de Receita e Ingredientes"""
    queryset = RltRecipeIngredient.objects.all()
    serializer_class = RltRecipeIngredientSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
