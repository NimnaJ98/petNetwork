from .models import Profile, Relationship

#show the profile picture next to the user
def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.avatar
        return {'picture':pic}
    return{}

#show no of invitations
def invitations_received(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        qs_count = Relationship.objects.invitations_received(profile_obj).count()
        return {'invites_num':qs_count}
    return{}