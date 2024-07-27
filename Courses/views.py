from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from Courses.forms import CourseCreateForm, CourseEditForm
from .models import Category, Course

# Create your views here.

def index(request):

    kategoriler = Category.objects.all()

    kurslar = Course.objects.filter(isActive=True, isHome=True)

    return render(request, "courses/index.html", {
        "courses": kurslar,
        "categories": kategoriler
    })

def search(request):

    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__icontains=q).order_by("date")
        kategoriler = Category.objects.all()

    else:
        return redirect("/kurs")

    return render(request, "courses/search.html", {
        "courses": kurslar,
        "categories": kategoriler
    })

def createCourse(request):
    
    if request.method == "POST":
        form = CourseCreateForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("/kurs")
        
    else:
        form = CourseCreateForm()  # Get request: sayfa ilk açıldığında boş form gösterilecek

    return render(request, "courses/create_course.html", {
        "form": form
    })

def courseList(request):
    
    kurslar =Course.objects.all()

    return render(request, "courses/course_list.html", {
        "courses": kurslar
    })

def courseEdit(request, id):
    course = get_object_or_404(Course, pk=id)

    form = CourseEditForm(instance=course)

    return render(request, "courses/course_edit.html", {
        "form": form
    })

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

    return render(request, "courses/list.html", {
        "page_obj": page_obj,
        "categories": kategoriler,
        "selected_category": slug
    })


