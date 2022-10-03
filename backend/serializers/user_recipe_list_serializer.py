from backend.serializers import *
from backend.models import Recipe


class UserRecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe.objects.all()
        fields = ['category', 'recipe_title']
