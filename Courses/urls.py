from django.http import HttpResponse
from django.urls import path

# http://127.0.0.1:8000/          -> Anasayfa
# http://127.0.0.1:8000/anasayfa  -> Anasayfa
# http://127.0.0.1:8000/kurslar   -> Kurslar Listesi

def home(request):
    return HttpResponse("Anasayfa")

def courses(request):
    return HttpResponse("Kurslar Listesi")

urlpatterns = [
    path("", home),
    path("anasayfa", home),
    path("kurslar", courses),
]