from django.urls import path, reverse_lazy

from .views import *

app_name = 'gallery'

urlpatterns = [
    path('', HomeGalleryView.as_view(), name='photo-gallery'),
    path('photo/<slug:slug>/', PhotoDetailView.as_view(), name='photo'),
    path('gallery/category/<slug:cat_slug>/', CategoryGalleryView.as_view(), name='category'),
]
