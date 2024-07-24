from django.contrib import admin
from .models import Category, Course

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'isActive', 'slug', 'category')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('isActive', 'category')
    list_editable = ('isActive',)
    search_fields = ('title', 'description')

