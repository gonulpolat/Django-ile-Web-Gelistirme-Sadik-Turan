from django.urls import path
from . import views

# http://127.0.0.1:8000              -> Anasayfa
# http://127.0.0.1:8000/anasayfa     -> Anasayfa
# http://127.0.0.1:8000/iletisim     -> İletişim Sayfası
# http://127.0.0.1:8000/hakkimizda   -> Hakkımızda Sayfası

urlpatterns = [
    path("", views.home),
    path("anasayfa", views.home),
    path("iletisim", views.contact),
    path("hakkimizda", views.about),
]