from django import forms
from django.forms import TextInput, Textarea

from Courses.models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'imageUrl', 'slug')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'imageUrl': 'Image URL',
            'slug': 'Slug'
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'imageUrl': TextInput(attrs={'class': 'form-control'}),
            'slug': TextInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            'title': {
                'required': 'Kurs başlığı girmelisiniz.',
                'max_length': 'Kurs başlığı en fazla 50 karakter olabilir.'
            },
            'description': {
                'required': 'Kurs açıklaması girmelisiniz.'
            },
            'imageUrl': {
                'required': 'Fotoğraf eklemelisiniz.',
                'max_length': 'Fotoğraf URL\'si en fazla 50 karakter olabilir.'
            }
        }


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'imageUrl', 'slug')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'imageUrl': 'Image URL',
            'slug': 'Slug'
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'imageUrl': TextInput(attrs={'class': 'form-control'}),
            'slug': TextInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            'title': {
                'required': 'Kurs başlığı girmelisiniz.',
                'max_length': 'Kurs başlığı en fazla 50 karakter olabilir.'
            },
            'description': {
                'required': 'Kurs açıklaması girmelisiniz.'
            },
            'imageUrl': {
                'required': 'Fotoğraf eklemelisiniz.',
                'max_length': 'Fotoğraf URL\'si en fazla 50 karakter olabilir.'
            }
        }
