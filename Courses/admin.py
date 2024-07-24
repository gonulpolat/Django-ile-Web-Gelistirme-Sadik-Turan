from django.contrib import admin
from .models import Category, Course

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'isActive', 'slug', 'category')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('isActive', 'category')
    list_editable = ('isActive',)
    search_fields = ('title', 'description')

