from backend.serializers import *
from backend.models import UnitOfMeasurement


class UnitOfMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = '__all__'


class UnitOfMeasurementFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = ['id', 'unit_of_measurement', 'initials']
