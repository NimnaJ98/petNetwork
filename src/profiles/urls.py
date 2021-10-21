from django.urls import path
from .views import pet_profile_view, invites_received_view, profiles_list_view, invite_profiles_list_view

app_name = 'profiles'

urlpatterns = [
    path('petProfile/', pet_profile_view, name='pet-profile-view'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('all-profiles/', profiles_list_view, name='all-profiles-view'),
    path('to-invite/', invite_profiles_list_view, name='invite-profiles-view'),
]

