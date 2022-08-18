from django.contrib import admin

from .models import Courses


class CoursesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'draft'
    ]
    list_filter = [
        'created',
        'updated'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Courses, CoursesAdmin)
