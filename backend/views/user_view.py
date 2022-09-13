from backend.views import *
from backend.serializers import UserSerializer
from backend.models import User


class UserView(viewsets.ModelViewSet):
    """Exibindo os Usuários"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
