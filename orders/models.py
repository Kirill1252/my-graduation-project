from courses.models import Courses
from django.db import models
from photo_gallery.models import PhotoGallery
from users.models import CustomUser


class Orders(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ForeignKey(PhotoGallery, on_delete=models.CASCADE, blank=True, null=True)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    processed = models.BooleanField(default=False)
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'User: {self.customer.username}'


class AnonymousFormOrders(models.Model):
    photo = models.ForeignKey(PhotoGallery, on_delete=models.CASCADE, blank=True, null=True)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    mobile = models.IntegerField(null=True, blank=True, )
    email = models.EmailField(null=True, blank=True, )
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f'Name: {self.name}'
