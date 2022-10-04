from rest_framework.response import Response
from rest_framework import status


def location(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        id = str(serializer.data['id'])
        response['Location'] = request.build_absolute_uri() + id
        return response