from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cover = models.ImageField(upload_to='CoursesCover/%Y/%m/%d')
    video_course = models.FileField(upload_to='VideoCourse/certificate/%Y/%m/%d')
    draft = models.BooleanField(default=False)

    def __str__(self):
        return f'Name courses: {self.name}'
