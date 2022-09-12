from backend.models import *


class Image(models.Model):
    image = models.ImageField(blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
