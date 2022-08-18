from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail

from .models import Courses
from photo_gallery.models import Category

from orders.forms import OrdersForm, AnonymousFormOrdersForms
from users.models import CustomUser


class CoursesView(ListView):
    paginate_by = 10
    model = Courses
    ordering = '-created'
    template_name = 'courses/courses_views.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Video courses'
        context['categorys'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Courses.objects.filter(draft=False)


class CourseDetailView(DetailView):
    template_name = 'courses/courses_detail.html'
    model = Courses
    context_object_name = 'course'

    def get_success_url(self):
        return reverse('courses:course', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Video courses'
        context['categorys'] = Category.objects.all()
        context['authenticated_form'] = OrdersForm()
        context['anonymous_form'] = AnonymousFormOrdersForms()
        return context

    def post(self, request, slug):
        if request.user.is_authenticated:
            r = self.request.user.pk
            authenticated_form = OrdersForm(request.POST, request.FILES)
            if authenticated_form.is_valid():
                course = Courses.objects.get(slug=slug)
                customer = CustomUser.objects.get(pk=r)
                orders = authenticated_form.save(commit=False)
                orders.courses = course
                orders.customer = customer
                orders.save()
                send_mail('У вас новый заказ',
                          f'''
                                         Новый заказ: {course.name}.
                                         Сумма заказа {course.price}$.
                                         Заказал {customer.email}
                                         ''',
                          'b75d4b9397e68a',
                          ['b75d4b9397e68a', ]
                          )
                return redirect('courses:courses')
        else:
            anonymous_form = AnonymousFormOrdersForms(request.POST, request.FILES)
            course = Courses.objects.get(slug=slug)
            orders = anonymous_form.save(commit=False)
            orders.courses = course
            orders.save()
            send_mail('У вас новый заказ',
                      f'''
                                     Новый заказ: {course.name}.
                                     Сумма заказа {course.price}$.
                                     Заказал {orders.name}.
                                     Номер телефона:{orders.mobile}.
                                     Email: {orders.email}
                                     ''',
                      'b75d4b9397e68a',
                      ['b75d4b9397e68a', ]
                      )
            return redirect('courses:courses')