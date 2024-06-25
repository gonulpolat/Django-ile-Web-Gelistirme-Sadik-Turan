from django.urls import path
from . import views

# http://127.0.0.1:8000/                 => anasayfa
# http://127.0.0.1:8000/home             => anasayfa
# http://127.0.0.1:8000/contact          => iletişim sayfası
# http://127.0.0.1:8000/about            => hakkımızda sayfası

urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("contact", views.contact),
    path("about", views.about),
]