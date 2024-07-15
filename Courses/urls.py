from django.urls import path
from . import views

# http://127.0.0.1:8000/kurs                    -> Kurslar Listesi
# http://127.0.0.1:8000/kurs/liste              -> Kurslar Listesi
# http://127.0.0.1:8000/kurs/detay              -> Kurs Detay Sayfası
# http://127.0.0.1:8000/kurs/programlama        -> Programlama Kurs Sayfası
# http://127.0.0.1:8000/kurs/mobil-uygulamalar  -> Mobil Uygulama Kurs Sayfası

urlpatterns = [
    path("", views.courses),
    path("liste", views.courses),
    path("detay", views.details),
    path("programlama", views.programming),
    path("mobil-uygulamalar", views.mobilapps),
]