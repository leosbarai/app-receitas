from backend.serializers import *
from backend.models import Recipe


class UserRecipeListSerializer(serializers.ModelSerializer):
    recipe = serializers.ReadOnlyField(source='recipe.recipe_title')
    category = serializers.ReadOnlyField(source='recipe.category')

    class Meta:
        model = Recipe.objects.all()
        fields = ['recipe', 'category']
