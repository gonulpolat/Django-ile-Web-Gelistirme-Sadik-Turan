from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses(request):
    return HttpResponse("Kurslar Listesi")

def details(request):
    return HttpResponse("Kurs Detay Sayfası")

def getCoursesByCategory(request, category_name):

    text = ""

    if category_name == "programlama":
        text = "Programlama kategorisine ait kurslar"
    elif category_name == "web-gelistirme":
        text = "Web Geliştirme kategorisine ait kurslar"
    else:
        text = "Bu kategoriye ait kurs bulunamadı"

    return HttpResponse(text)

def getCoursesByCategoryId(request, category_id):
    return HttpResponse(category_id)