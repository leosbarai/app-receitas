from backend.models import *


class Recipe(models.Model):
    recipe_title = models.CharField(max_length=30)
    efficiency = models.CharField(max_length=30)
    preparation_time = models.CharField(max_length=10)
    preparation_instructions = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.recipe_title)
