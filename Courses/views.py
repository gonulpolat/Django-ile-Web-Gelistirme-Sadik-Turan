from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("anasayfa")

def courses(request):
    return HttpResponse("kurs listesi")

def contact(request):
    return HttpResponse("iletişim sayfası")

def about(request):
    return HttpResponse("hakkımızda sayfası")