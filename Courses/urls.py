from django.urls import path
from . import views

# http://127.0.0.1:8000/kurslar     -> Kurslar Listesi

urlpatterns = [
    path("kurslar", views.courses),
]