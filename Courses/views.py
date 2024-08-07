from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test

from Courses.forms import CourseCreateForm, CourseEditForm, CourseUploadForm
from .models import Category, Course, Slider, Upload

# Create your views here.

def index(request):

    kategoriler = Category.objects.all()

    kurslar = Course.objects.filter(isActive=True, isHome=True)

    sliders = Slider.objects.filter(isActive=True)

    return render(request, "courses/index.html", {
        "courses": kurslar,
        "categories": kategoriler,
        "sliders": sliders
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

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def createCourse(request):
    
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect("/kurs")
        
    else:
        form = CourseCreateForm()  # Get request: sayfa ilk açıldığında boş form gösterilecek

    return render(request, "courses/create_course.html", {
        "form": form
    })

@login_required()
def courseList(request):
    
    kurslar =Course.objects.all()

    return render(request, "courses/course_list.html", {
        "courses": kurslar
    })

def courseEdit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance=course)
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

        form = CourseUploadForm(request.POST, request.FILES)

        if form.is_valid():
            image = Upload(image=request.FILES["image"])
            image.save()
           
            return render(request, "courses/success.html")
    
    else:
        form = CourseUploadForm()
    
    return render(request, "courses/upload.html", {
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


