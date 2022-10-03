from backend.serializers import *
from backend.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ImageSerializerFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']
