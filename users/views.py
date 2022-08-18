from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from photo_gallery.models import Category

from .forms import RegisterUserForm, LoginForm, UpdateUserData
from .models import CustomUser


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register_user.html'

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST, request.FILES)
        user = form.save(commit=False)
        user.email = user.username
        user.slug = user.username.split('@')[0]
        user.save()
        group = Group.objects.get(name='groups_user')
        user.groups.add(group)
        login(self.request, user)
        return redirect('gallery:photo-gallery')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        context['categorys'] = Category.objects.all()
        return context


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['categorys'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('gallery:photo-gallery')


class UserPageView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    login_url = reverse_lazy('user:login')
    model = CustomUser
    template_name = 'user/user_page.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User page'
        context['categorys'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse('user:profile', kwargs={'slug': self.object.slug})

    def test_func(self):
        user_slug = self.kwargs['slug']
        user = self.request.user.slug
        custom_user = CustomUser.objects.get(slug=user_slug)
        if custom_user.slug != user:
            return False
        return True


class UpdateAuthorProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = reverse_lazy('user:login')
    model = CustomUser
    form_class = UpdateUserData
    template_name = 'user/creating_user_profile.html'

    def test_func(self):
        user_slug = self.kwargs['slug']
        user = self.request.user.slug
        custom_user = CustomUser.objects.get(slug=user_slug)
        if custom_user.slug != user:
            return False
        return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update profile'
        context['categorys'] = Category.objects.all()
        return context
