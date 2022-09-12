from backend.serializers import *
from backend.models import UnitOfMeasurement


class UnitOfMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = '__all__'
