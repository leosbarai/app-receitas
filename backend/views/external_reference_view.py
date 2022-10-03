from backend.views import *
from backend.models import ExternalReference
from backend.serializers import ExternalReferenceSerializer


class ExternalReferenceViewSet(viewsets.ModelViewSet):
    """Exibindo as referências externas"""
    queryset = ExternalReference.objects.all()
    serializer_class = ExternalReferenceSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
