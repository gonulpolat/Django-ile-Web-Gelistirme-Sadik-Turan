from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.

data = {
    "programlama": "Programlama kategorisine ait kurslar",
    "web-gelistirme": "Web Geliştirme kategorisine ait kurslar",
    "mobil-uygulamalar": "Mobil Uygulamalar kategorisine ait kurslar"
}

def courses(request):
    return HttpResponse("Kurslar Listesi")

def details(request, course_name):
    return HttpResponse(f"{course_name} detay sayfası")

def getCoursesByCategory(request, category_name):

    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("Yanlış kategori seçimi")

def getCoursesByCategoryId(request, category_id):

    category_list = list(data.keys())

    if category_id > len(category_list) or category_id < 1:
        return HttpResponseNotFound("Yanlış kategori seçimi")
    
    category_name = category_list[category_id - 1]

    redirect_url = reverse("courses_by_category", args=[category_name])

    return redirect(redirect_url)