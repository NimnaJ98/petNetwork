from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.deletion import CASCADE
from profiles.models import Profile

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to ='posts', validators = [FileExtensionValidator(['png','jpg','jpeg'])], blank = True)
    liked = models.ManyToManyField(Profile, blank=True, related_name='Likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=CASCADE, related_name='posts')

    def __str__(self):
        return str(self.content[:20])

#to grab the number of likes
    def num_likes(self):
        return self.liked.all().count()

#to grab the number of comments
    def num_comments(self):
        return self.comment_set.all().count()


#to create the ordering of the posts by time
    class Meta:
        ordering = ('-created',)



class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.pk)


LIKE_CHOICES = (
    #value for processing vs value we see
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"




