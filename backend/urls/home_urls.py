from django.urls import path
from backend.views.home_view import home_view

urlpatterns = [
    path("", home_view),
]
