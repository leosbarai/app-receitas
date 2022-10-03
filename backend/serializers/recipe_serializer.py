from backend.serializers import *
from backend.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'recipe_title', 'efficiency', 'preparation_time', 'preparation_instructions', 'category']
