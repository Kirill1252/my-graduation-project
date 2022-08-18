from django.urls import path, reverse_lazy

from .views import *

app_name = 'courses'

urlpatterns = [
    path('video/course/', CoursesView.as_view(), name='courses'),
    path('video/course/<slug:slug>/', CourseDetailView.as_view(), name='course')
]