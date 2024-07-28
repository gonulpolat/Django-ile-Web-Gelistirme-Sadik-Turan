import os
import random
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

    if request.method == "POST":
        form = CourseEditForm(request.POST, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)

    return render(request, "courses/course_edit.html", {
        "form": form
    })

def courseDelete(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "courses/course_delete.html", {
        "course": course
    })

def upload(request):

    if request.method == "POST":
        uploaded_images = request.FILES.getlist("images")
        for image in uploaded_images:
            handle_uploaded_file(image)
        return render(request, "courses/success.html")
    
    return render(request, "courses/upload.html")

def handle_uploaded_file(file):
    """
    Dosya isimleri random sayılarla oluşturulacak.
    Aynı isimde dosya yüklenirse de farklı isimlerle kaydedilecek.
    """

    number = random.randint(1, 99999)
    file_name, file_extension = os.path.splitext(file.name)
    name = file_name + "_" + str(number) + file_extension
    with open("temp/" + name, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

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


