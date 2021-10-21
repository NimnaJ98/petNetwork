from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import default, slugify
from django.db.models import Q

# Create your models here.
class ProfileManager(models.Manager):

    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))
        print(qs)
        print("#########")

        accepted= set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)
        print("#########")

        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        print("#########")
        return available


    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles

class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=200, blank=True)
    bio = models.TextField(default="no bio...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    avatar = models.ImageField(default = 'avatar_pet.png', upload_to='')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

    #to grab all the friends to show in petProfile
    def get_friends(self):
        return self.friends.all()

    #to grab all the count of friends to show in petProfile
    def get_friends_no(self):
        return self.friends.all().count()

    #to grab all the count of posts to show in petProfile
    def get_post_no(self):
        return self.posts.all().count()

    #to grab all the posts to show in petProfile
    def get_all_authors_posts(self):
        return self.posts.all()

    #to grab the no of likes given by the user
    def get_likes_given_no(self):
        Likes = self.like_set.all()
        total_liked = 0
        for item in Likes:
            if item.value == 'Like':
                total_liked += 1
        return total_liked

    #to grab the no of likes the user was received
    def get_likes_received_no(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.like_set.all().count()
        return total_liked

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%y')}"


    def save(self, *args, **kwargs):
        ex =False
        if self.name:
            to_slug = slugify(str(self.name))
            ex = Profile.objects.filter(slug = to_slug).exists()
            while ex:
                to_slug = slugify(to_slug+" "+ str(get_random_code()))
                ex = Profile.objects.filter(slug = to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)

STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted')
)

class RelationshipManager(models.Manager):
    def invitations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs 


class Relationship(models.Model):
    
    #everytime a particular profile is deleted, the relationship will also be deleted. 
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')

    #to determine the status of the choice. whether it's a sent invitation or an invitation accepted
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()



    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"