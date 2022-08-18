from django.db import models
from django.urls import reverse


class Category(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery:category', kwargs={'cat_slug': self.slug})


class Tag(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class PhotoGallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    photo = models.ImageField(upload_to='PhotoGallery/%Y/%m/%d')
    certificate = models.FileField(upload_to='PhotoGallery/certificate/%Y/%m/%d')
    draft = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery:photo', kwargs={'slug': self.slug})
