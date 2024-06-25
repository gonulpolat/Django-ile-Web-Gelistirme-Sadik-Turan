from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses(request):
    return HttpResponse("kurs listesi")

def details(request):
    return HttpResponse("kurs detay sayfası")

def programming(request):
    return HttpResponse("programlama kurs listesi")

def mobile_apps(request):
    return HttpResponse("mobil uygulamalar kurs listesi")

