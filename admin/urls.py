from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from backend.views.profile_view import ProfileViewSet
from backend.views.category_view import CategoriesViewSet
from backend.views.external_reference_view import ExternalReferenceViewSet
from backend.views.image_view import ImageViewSet
from backend.views.ingredient_view import IngredientViewSet
from backend.views.unit_of_measurement_view import UnitOfMeasurementViewSet
from backend.views.recipe_view import RecipeViewSet
from backend.views.rlt_recipe_ingredient_view import RltRecipeIngredientViewSet
from backend.views.user_recipe_list_view import UserRecipeListViewSet


router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, basename='Profiles')
router.register('category', CategoriesViewSet, basename='Categories')
router.register('external_reference', ExternalReferenceViewSet, basename='ExternalReferences')
router.register('image', ImageViewSet, basename='Images')
router.register('ingredient', IngredientViewSet, basename='Ingredients')
router.register('unit_of_measurement', UnitOfMeasurementViewSet, basename='UnitOfMeasurements')
router.register('recipe', RecipeViewSet, basename='Recipes')
router.register('rlt_recipe_ingredient', RltRecipeIngredientViewSet, basename='RltRecipeIngredients')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/<int:pk>/recipes/', UserRecipeListViewSet.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
