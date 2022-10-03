from backend.views import *
from backend.serializers import ProfileSerializer
from backend.models import Profile



class ProfileViewSet(viewsets.ModelViewSet):
    """Exibindo os Usuários"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
