from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    fullname = models.CharField(max_length=200, blank=True)
    # owner رو از Profile حذف کردیم چون مربوط به محصوله و باید توی مدل Product باشه
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')
    bio = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.user.username



def user_directory_path(instance, filename):
    return f'profile_pics/user_{instance.user.id}/{filename}'
