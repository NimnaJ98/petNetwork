from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=200, blank=True)
    bio = models.TextField(default="no bio...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    avatar = models.ImageField(default = 'avatar.png', upload_to='')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    #to grab all the friends to show in petProfile
    def get_friends(self):
        return self.friends.all()

    #to grab all the count of friends to show in petProfile
    def get_friends_no(self):
        return self.friends.all().count()


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

class Relationship(models.Model):
    
    #everytime a particular profile is deleted, the relationship will also be deleted. 
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')

    #to determine the status of the choice. whether it's a sent invitation or an invitation accepted
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"