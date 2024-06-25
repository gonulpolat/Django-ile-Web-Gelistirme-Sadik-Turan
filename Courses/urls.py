from django.urls import path
from . import views

# http://127.0.0.1:8000/                => anasayfa
# http://127.0.0.1:8000/client          => anasayfa
# http://127.0.0.1:8000/home            => anasayfa
# http://127.0.0.1:8000/client/home     => anasayfa
# http://127.0.0.1:8000/courses         => kurs listesi
# http://127.0.0.1:8000/client/courses  => kurs listesi


urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("courses", views.courses),
]
