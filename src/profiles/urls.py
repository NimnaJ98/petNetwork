from django.urls import path
from .views import pet_profile_view

app_name = 'profiles'

urlpatterns = [
    path('petProfile/', pet_profile_view, name='pet-profile-view')
]

