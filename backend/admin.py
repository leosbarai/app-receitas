from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role')
    list_display_links = ('id', 'user', 'role')
    search_fields = ('user', 'email',)
    list_per_page = 20


admin.site.register(Profile, ProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'active')
    list_display_links = ('id', 'category')
    search_fields = ('category', 'active',)
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)


class ExternalReferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'recipe', 'active')
    list_display_links = ('id', 'link', 'recipe')
    search_fields = ('id', 'recipe', 'active',)
    list_per_page = 20


admin.site.register(ExternalReference, ExternalReferenceAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'recipe', 'active')
    list_display_links = ('id', 'image', 'recipe')
    search_fields = ('id', 'recipe', 'active',)
    list_per_page = 20


admin.site.register(Image, ImageAdmin)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'active')
    list_display_links = ('id', 'ingredient')
    search_fields = ('id', 'ingredient', 'active',)
    list_per_page = 20


admin.site.register(Ingredient, IngredientAdmin)


class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_of_measurement', 'initials', 'active',)
    list_display_links = ('id', 'unit_of_measurement', 'initials')
    search_fields = ('unit_of_measurement', 'initials', 'active',)
    list_per_page = 20


admin.site.register(UnitOfMeasurement, UnitOfMeasureAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe_title', 'efficiency', 'preparation_time', 'preparation_instructions', 'category',
                    'active', 'user')
    list_display_links = ('id', 'recipe_title', 'user')
    search_fields = ('id', 'recipe_title', 'active', 'user', 'active',)
    list_per_page = 20


admin.site.register(Recipe, RecipeAdmin)


class RltRecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'unit_of_measurement', 'quantity', 'active')
    list_display_links = ('id', 'recipe', 'ingredient', 'unit_of_measurement')
    search_fields = ('recipe', 'ingredient', 'unit_of_measurement', 'quantity', 'active',)
    list_per_page = 20


admin.site.register(RltRecipeIngredient, RltRecipeIngredientAdmin)
