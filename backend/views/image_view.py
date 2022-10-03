from backend.views import *
from backend.serializers import ImageSerializer
from backend.models import Image


class ImageViewSet(viewsets.ModelViewSet):
    """Exibindo as imagens"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['image']
    search_fields = ['image']
    filterset_fields = ['active']
