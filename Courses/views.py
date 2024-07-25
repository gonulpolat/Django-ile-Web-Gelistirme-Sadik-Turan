from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Category, Course

# Create your views here.

def index(request):

    kategoriler = Category.objects.all()

    kurslar = Course.objects.filter(isActive=True)

    return render(request, "courses/index.html", {
        "courses": kurslar,
        "categories": kategoriler
    })

def search(request):

    print(request.GET)   
    # http://127.0.0.1:8000/kurs/search?q=python                --> <QueryDict: {'q': ['python']}>
    # http://127.0.0.1:8000/kurs/search?q=python&order_by=date  --> <QueryDict: {'q': ['python'], 'order_by': ['date']}>

    print(request.GET.get("q"))        # python
    print(request.GET.get("order_by")) # date

def details(request, slug):
    
    course = get_object_or_404(Course, slug=slug)

    context = {
        "course": course
    }

    return render(request, "courses/details.html", context)

def getCoursesByCategory(request, slug):

    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 2)
    page = request.GET.get("page", 1)
    page_obj = paginator.page(page)

    return render(request, "courses/index.html", {
        "page_obj": page_obj,
        "categories": kategoriler,
        "selected_category": slug
    })


