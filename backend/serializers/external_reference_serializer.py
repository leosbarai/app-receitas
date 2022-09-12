from backend.serializers import *
from backend.models import ExternalReference


class ExternalReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalReference
        fields = '__all__'
