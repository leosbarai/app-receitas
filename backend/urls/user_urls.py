from django.urls import path
from backend.views.profile_view import list_profile_view


urlpatterns = [
    path("", list_profile_view, name='users'),
    path("<int:id>", list_profile_view, name='user'),
]
