from backend.models import *


class UnitOfMeasurement(models.Model):
    unit_of_measurement = models.CharField(max_length=30)
    initials = models.CharField(max_length=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.unit_of_measurement)
