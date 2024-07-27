from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(
        label="Başlık", 
        required=True,
        error_messages={"required": "Kurs başlığı zorunludur."},
        widget=forms.TextInput()  # default widget
        )
    description = forms.CharField(widget=forms.Textarea)
    imageUrl = forms.CharField()
    slug = forms.SlugField()
