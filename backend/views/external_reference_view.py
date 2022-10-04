from backend.views import *
from backend.models import ExternalReference
from backend.serializers import ExternalReferenceSerializer


class ExternalReferenceViewSet(viewsets.ModelViewSet):
    """Exibindo as referências externas"""
    queryset = ExternalReference.objects.all()
    serializer_class = ExternalReferenceSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
