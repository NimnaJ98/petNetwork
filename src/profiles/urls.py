from django.urls import path
from .views import (
    pet_profile_view, 
    invites_received_view, 
    profiles_list_view, 
    invite_profiles_list_view, 
    ProfileDetailView,
    ProfileListView, 
    send_invitations, 
    remove_from_friends,
    accept_invitation,
    reject_invitation,
)

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='all-profiles-view'),
    path('petProfile/', pet_profile_view, name='pet-profile-view'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('to-invite/', invite_profiles_list_view, name='invite-profiles-view'),
    path('send-invite/',send_invitations, name='send-invite'),
    path('remove-friend/',remove_from_friends, name='remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('my-invites/accept/', accept_invitation, name='accept-invite'),
    path('my-invites/reject/', reject_invitation, name='reject-invite'),
]

