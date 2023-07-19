from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User= get_user_model() # model of the currently logged in user

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # connect the user model to the profile model as Foreign Key
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username #jb hm isko admin panel me dekhenge to username dikhega na ki object 1 , object 2
    # def __unicode__(self):
        # return u'Profile of user: %s' % self.user.username

class Post(models.Model):
    id=  models.UUIDField(primary_key=True,default=uuid.uuid4)
    user= models.CharField(max_length=100)
    image= models.ImageField(upload_to ="post_images")
    caption= models.TextField()
    created_at= models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
