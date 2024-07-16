from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses(request):
    return HttpResponse("Kurslar Listesi")

def details(request):
    return HttpResponse("Kurs Detay Sayfası")

def getCoursesByCategory(request, category):

    text = ""

    if category == "programlama":
        text = "Programlama kategorisine ait kurslar"
    elif category == "web-gelistirme":
        text = "Web Geliştirme kategorisine ait kurslar"
    else:
        text = "Bu kategoriye ait kurs bulunamadı"

    return HttpResponse(text)