from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars')
    bio = models.TextField(verbose_name='Bio')
    location = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username