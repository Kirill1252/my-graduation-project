from django.contrib import admin

from .models import Orders, AnonymousFormOrders


class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'processed',
    ]
    list_display_links = [
        'customer',
        'processed',
    ]
    list_filter = [
        'processed',
        'created',
        'updated',
    ]
    readonly_fields = [
        'customer',
        'photo',
        'courses'
    ]
    search_fields = ('customer__username', 'customer__mobile')


admin.site.register(Orders, OrdersAdmin)


class AnonymousOrdersAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'processed',
    ]
    list_display_links = [
        'name',
        'processed',
    ]
    readonly_fields = [
        'name',
        'photo',
        'courses',
        'email',
        'mobile'
    ]


admin.site.register(AnonymousFormOrders, AnonymousOrdersAdmin)

