from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role')
    list_display_links = ('id', 'user', 'role')
    search_fields = ('user', 'email',)
    list_per_page = 20


admin.site.register(Profile, ProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('id', 'category')
    search_fields = ('category',)
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)


class ExternalReferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'link')
    list_display_links = ('id', 'link')
    list_per_page = 20


admin.site.register(ExternalReference, ExternalReferenceAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    list_display_links = ('id', 'image')
    list_per_page = 20


admin.site.register(Image, ImageAdmin)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient')
    list_display_links = ('id', 'ingredient')
    search_fields = ('ingredient',)
    list_per_page = 20


admin.site.register(Ingredient, IngredientAdmin)


class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_of_measurement', 'initials')
    list_display_links = ('id', 'unit_of_measurement', 'initials')
    search_fields = ('unit_of_measurement', 'initials',)
    list_per_page = 20


admin.site.register(UnitOfMeasurement, UnitOfMeasureAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe_title')
    list_display_links = ('id', 'recipe_title')
    search_fields = ('recipe_title',)
    list_per_page = 20


admin.site.register(Recipe, RecipeAdmin)


class RltRecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe')
    list_display_links = ('id', 'recipe')
    search_fields = ('recipe',)
    list_per_page = 20


admin.site.register(RltRecipeIngredient, RltRecipeIngredientAdmin)
