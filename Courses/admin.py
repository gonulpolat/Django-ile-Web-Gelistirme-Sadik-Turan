from django.contrib import admin
from .models import Category, Course

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'isActive', 'slug')
    list_display_links = ('title', 'slug')
    readonly_fields = ('slug',)
    list_filter = ('isActive',)
    list_editable = ('isActive',)
    search_fields = ('title', 'description')

