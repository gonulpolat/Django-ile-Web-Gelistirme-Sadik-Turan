from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Anasayfa")

def courses(request):
    return HttpResponse("Kurslar Listesi")

def contact(request):
    return HttpResponse("İletişim Sayfası")

def about(request):
    return HttpResponse("Hakkımızda Sayfası")