from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True)
    mobile = models.IntegerField(null=True, blank=True, )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user:profile', kwargs={'slug': self.slug})
