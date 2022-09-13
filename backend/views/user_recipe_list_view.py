from backend.views import *
from backend.serializers import UserRecipeListSerializer
from backend.models import Recipe


class UserRecipeListView(generics.ListAPIView):
    """Listando Receitas do Usuário"""

    def get_queryset(self):
        queryset = Recipe.objects.filter(user_id=self.kwargs['pk'])
        return queryset

    serializer_class = UserRecipeListSerializer
