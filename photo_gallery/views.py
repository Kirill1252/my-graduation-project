from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from orders.forms import OrdersForm, AnonymousFormOrdersForms
from users.models import CustomUser

from .models import PhotoGallery, Category
from .telegram import send_telegram


class HomeGalleryView(ListView):
    paginate_by = 30
    model = PhotoGallery
    ordering = '-created'
    template_name = 'photo_gallery/photo-gallery.html'
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gallery'
        context['categorys'] = Category.objects.all()
        return context

    def get_queryset(self, **kwargs):
        search_query = self.request.GET.get('search', )
        if search_query:
            for items in search_query.split():
                context = PhotoGallery.objects.filter(Q(tag__name__icontains=items), draft=False)
                return context

        return PhotoGallery.objects.filter(draft=False)


class CategoryGalleryView(ListView):
    paginate_by = 30
    model = PhotoGallery
    ordering = '-created'
    template_name = 'photo_gallery/photo-gallery.html'
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gallery'
        context['categorys'] = Category.objects.all()
        return context

    def get_queryset(self):
        return PhotoGallery.objects.filter(category__slug=self.kwargs['cat_slug'], draft=False)


class PhotoDetailView(DetailView):
    template_name = 'photo_gallery/photo.html'
    model = PhotoGallery
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('gallery:photo', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Photo'
        context['categorys'] = Category.objects.all()
        context['authenticated_form'] = OrdersForm()
        context['anonymous_form'] = AnonymousFormOrdersForms()
        return context

    def post(self, request, slug):
        if request.user.is_authenticated:
            r = self.request.user.pk
            authenticated_form = OrdersForm(request.POST, request.FILES)
            if authenticated_form.is_valid():
                photo = PhotoGallery.objects.get(slug=slug)
                customer = CustomUser.objects.get(pk=r)
                orders = authenticated_form.save(commit=False)
                orders.photo = photo
                orders.customer = customer
                orders.save()
                mess_tel = (f'''
                      У вас новый заказ!!!
                      id_photo: {photo.pk}
                      Photo title: {photo.title}.
                      Сумма заказа: {photo.price}$.
                      Заказал: {customer.slug}.
                      Номер телефона:{customer.mobile}
                      Email {customer.email}.
                      ''')
                send_telegram(mess_tel)
                return redirect('gallery:photo-gallery')
        else:
            anonymous_form = AnonymousFormOrdersForms(request.POST, request.FILES)
            photo = PhotoGallery.objects.get(slug=slug)
            orders = anonymous_form.save(commit=False)
            orders.photo = photo
            orders.save()
            mess_tel = (f'''
                      У вас новый заказ!!!
                      id_photo:  {photo.pk}
                      Photo title: {photo.title}.
                      Сумма заказа: {photo.price}$.
                      Заказал {orders.name}.
                      Номер телефона:{orders.mobile}.
                      Email: {orders.email}
                      ''')
            send_telegram(mess_tel)
            return redirect('gallery:photo-gallery')
