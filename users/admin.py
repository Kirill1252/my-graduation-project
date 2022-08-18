from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from orders.models import Orders

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class OrdersInline(admin.TabularInline):
    model = Orders


class CustomUserAdmin(UserAdmin):
    inlines = [OrdersInline]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    search_fields = ('username', 'email', 'mobile')
    prepopulated_fields = {'username': ('email',)}
    list_display = ('username', 'email', 'mobile')
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        ('Custom fields', {
            'fields': (
                'slug',
                'instagram',
                'fecebook',
                'avatar',
                'mobile'
            )
        })
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        ('Custom fields', {
            'fields': (
                'slug',
                'instagram',
                'fecebook',
                'avatar',
                'mobile'
            )
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)
