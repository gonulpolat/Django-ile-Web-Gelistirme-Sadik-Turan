from django.http import HttpResponse
from django.urls import path


# http://127.0.0.1:8000/                => anasayfa
# http://127.0.0.1:8000/client          => anasayfa
# http://127.0.0.1:8000/home            => anasayfa
# http://127.0.0.1:8000/client/home     => anasayfa
# http://127.0.0.1:8000/courses         => kurs listesi
# http://127.0.0.1:8000/client/courses  => kurs listesi


def home(request):
    return HttpResponse("anasayfa")

def courses(request):
    return HttpResponse("kurs listesi")

urlpatterns = [
    path("", home),
    path("home", home),
    path("courses", courses),
]
