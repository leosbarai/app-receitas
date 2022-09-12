from backend.serializers import *
from backend.models import RltRecipeIngredient


class RltRecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RltRecipeIngredient
        fields = '__all__'
