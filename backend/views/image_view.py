from backend.views import *
from backend.serializers import ImageSerializer
from backend.models import Image


class ImageView(viewsets.ModelViewSet):
    """Exibindo as imagens"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
