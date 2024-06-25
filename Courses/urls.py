from django.urls import path
from . import views

# http://127.0.0.1:8000/courses                  => kurs listesi
# http://127.0.0.1:8000/courses/listes           => kurs listesi
# http://127.0.0.1:8000/courses/details          => kurs detay sayfası
# http://127.0.0.1:8000/courses/programming      => programlama kurs listesi
# http://127.0.0.1:8000/courses/mobile-apps      => mobil uygulamalar kurs listesi


urlpatterns = [
    path("", views.courses),
    path("listes", views.courses),
    path("details", views.details),
    path("programming", views.programming),
    path("mobile-apps", views.mobile_apps),
]
