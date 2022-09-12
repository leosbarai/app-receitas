from backend.serializers import *
from backend.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['id', 'category']
