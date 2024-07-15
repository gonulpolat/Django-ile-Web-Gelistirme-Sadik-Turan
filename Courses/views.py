from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses(request):
    return HttpResponse("Kurslar Listesi")

def details(request):
    return HttpResponse("Kurs Detay Sayfası")

def programming(request):
    return HttpResponse("Programlama Kurs Sayfası")

def mobilapps(request):
    return HttpResponse("Mobil Uygulama Kurs Sayfası")