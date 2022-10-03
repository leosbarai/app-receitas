from backend.views import *
from backend.serializers import ProfileSerializer
from backend.models import Profile



class ProfileViewSet(viewsets.ModelViewSet):
    """Exibindo os Usuários"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
