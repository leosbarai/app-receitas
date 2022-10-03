from backend.serializers import *
from backend.models import RltRecipeIngredient


class RltRecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RltRecipeIngredient
        fields = '__all__'


class RltRecipeIngredientFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RltRecipeIngredient
        fields = ['id', 'ingredient', 'unit_of_measurement', 'quantity']
