from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from backend.views.category_view import CategoriesViewSet
from backend.views.external_reference_view import ExternalReferenceView
from backend.views.image_view import ImageView
from backend.views.ingredient_view import IngredientView
from backend.views.unit_of_measurement_view import UnitOfMeasurementView
from backend.views.recipe_view import RecipeView
from backend.views.rlt_recipe_ingredient_view import RltRecipeIngreditView


router = routers.DefaultRouter()
router.register('category', CategoriesViewSet, basename='Categories')
router.register('external_reference', ExternalReferenceView, basename='ExternalReferences')
router.register('image', ImageView, basename='Images')
router.register('ingredient', IngredientView, basename='Ingredients')
router.register('unit_of_measurement', UnitOfMeasurementView, basename='UnitOfMeasurements')
router.register('recipe', RecipeView, basename='Recipes')
router.register('rlt_recipe_ingredient', RltRecipeIngreditView, basename='RltRecipeIngredients')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    # path('', include('backend.urls.home_urls')),
    # path('user/', include('backend.urls.user_urls')),
    # path('category/', include('backend.urls.user_urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
