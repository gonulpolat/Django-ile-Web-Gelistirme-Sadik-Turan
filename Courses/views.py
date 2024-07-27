from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
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
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl = request.POST["imageUrl"]
        slug = request.POST["slug"]
        isActive = request.POST.get("isActive", False)
        isHome = request.POST.get("isHome", False)
        
        if isActive == "on":
            isActive = True
    
        if isHome == "on":
            isHome = True

        error = False
        msg = ""

        if title == "":
            error = True
            msg = "Başlık boş olamaz."

        elif len(title) < 3:
            error = True
            msg = "Başlık en az 3 karakter olmalıdır."

        if error:
            return render(request, "courses/create_course.html", {
                "error": True,
                "msg": msg
            })

        course = Course(title=title, description=description, imageUrl=imageUrl, slug=slug, isActive=isActive, isHome=isHome)

        course.save()

        return redirect("/kurs")

    return render(request, "courses/create_course.html")


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


