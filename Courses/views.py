from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses(request):
    return HttpResponse("kurs listesi")

def details(request):
    return HttpResponse("kurs detay sayfası")

def getCourseByCategoryName(request, category_name):
    text = ""

    if category_name == "programming":
        text = "programlama"
    elif category_name == "design":
        text = "tasarım"
    elif category_name == "business":
        text = "işletme"
    else:
        text = "bilinmeyen"
    return HttpResponse(f"{text} kurs sayfası")

def getCourseByCategoryId(request, category_id):
    return HttpResponse(category_id)

