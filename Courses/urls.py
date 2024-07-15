from django.urls import path
from . import views

# http://127.0.0.1:8000/          -> Anasayfa
# http://127.0.0.1:8000/anasayfa  -> Anasayfa
# http://127.0.0.1:8000/kurslar   -> Kurslar Listesi



urlpatterns = [
    path("", views.home),
    path("anasayfa", views.home),
    path("kurslar", views.courses),
]