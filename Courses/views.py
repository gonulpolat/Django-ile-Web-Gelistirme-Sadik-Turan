from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses(request):
    return HttpResponse("kurs listesi")

def details(request):
    return HttpResponse("kurs detay sayfası")

def getCourseByCategory(request, category):
    text = ""

    if category == "programming":
        text = "programlama"
    elif category == "design":
        text = "tasarım"
    elif category == "business":
        text = "işletme"
    else:
        text = "bilinmeyen"
    return HttpResponse(f"{text} kurs sayfası")

