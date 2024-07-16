from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses(request):
    return HttpResponse("Kurslar Listesi")

def details(request):
    return HttpResponse("Kurs Detay Sayfası")

def getCoursesByCategory(request, category):
    return HttpResponse(f"{category} kategorisine ait kurs listesi")