from backend.serializers import *
from backend.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']
