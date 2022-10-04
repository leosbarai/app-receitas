from backend.views import *
from backend.serializers import ImageSerializer
from backend.models import Image


class ImageViewSet(viewsets.ModelViewSet):
    """Exibindo as imagens"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['image']
    search_fields = ['image']
    filterset_fields = ['active']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
