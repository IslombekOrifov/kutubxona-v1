from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import Course, CourseApplication


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ('name', 'duration', 'amount', 'is_online', 'is_active', 'created')
    list_filter = ('created',)
    ordering = ('amount', 'is_active', 'is_online', 'created')
    fieldsets = (
        ('Translateble', {
          'fields': ('name', 'sub_name', 'duration', 'description')
        }),
        ('Standard info', {
            'fields': ('image', 'amount', 'is_online', 'is_active')
        }),
      
    )
    

@admin.register(CourseApplication)
class CourseApplicationAdmin(admin.ModelAdmin):
    list_display = ('course', 'full_name', 'phone', 'region', 'is_checked', 'created')
    list_filter = ('created',)
    ordering = ('course', 'region', 'is_checked', 'created')