from django import forms
from django.forms import SelectMultiple, TextInput, Textarea

from Courses.models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image URL',
            'slug': 'Slug'
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'slug': TextInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            'title': {
                'required': 'Kurs başlığı girmelisiniz.',
                'max_length': 'Kurs başlığı en fazla 50 karakter olabilir.'
            },
            'description': {
                'required': 'Kurs açıklaması girmelisiniz.'
            }
        }


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug', 'categories', 'isActive', 'isHome')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image URL',
            'slug': 'Slug'
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'slug': TextInput(attrs={'class': 'form-control'}),
            'categories': SelectMultiple(attrs={'class': 'form-control'})
        }
        error_messages = {
            'title': {
                'required': 'Kurs başlığı girmelisiniz.',
                'max_length': 'Kurs başlığı en fazla 50 karakter olabilir.'
            },
            'description': {
                'required': 'Kurs açıklaması girmelisiniz.'
            }
        }

    
class CourseUploadForm(forms.Form):
    image = forms.FileField()
