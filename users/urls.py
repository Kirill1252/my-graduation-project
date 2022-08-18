from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from .views import *

app_name = 'user'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('user:login')), name='logout'),
    path('profile/<slug:slug>/', UserPageView.as_view(), name='profile'),
    path('profile/<slug:slug>/update/', UpdateAuthorProfileView.as_view(), name='update_user'),
]