from datetime import date, datetime
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Category, Course

# Create your views here.

data = {
    "programlama": "Programlama kategorisine ait kurslar",
    "web-gelistirme": "Web Geliştirme kategorisine ait kurslar",
    "mobil-uygulamalar": "Mobil Uygulamalar kategorisine ait kurslar"
}

db = {
    "courses": [
        {
            "title": "Javascript Kursu",
            "description": "JavaScript, geliştiricilerin etkileşimli web sayfaları oluşturmak için kullandığı bir programlama dilidir. JavaScript işlevleri, sosyal medya akışlarını yenilemekten animasyonlar ve etkileşimli haritalar göstermeye kadar, bir web sitesi kullanıcısının deneyimini iyileştirebilir.",
            "imageUrl": "javascript.png",
            "slug": "javascript-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": True
        },
        {
            "title": "Python Kursu",
            "description": "Python; web uygulamaları, yazılım geliştirme, veri bilimi ve makine öğreniminde (ML) yaygın olarak kullanılan bir programlama dilidir. Geliştiriciler, etkili ve öğrenmesi kolay olduğu ve birçok farklı platformda çalıştırılabildiği için Python'ı kullanır.",
            "imageUrl": "python.png",
            "slug": "python-kursu",
            "date": date(2024, 4, 26),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "Php Kursu",
            "description": "PHP (Hypertext Preprocessor), yaygın olarak kullanılan web tabanlı ve açık kaynak kodlu bir programlama dilidir.",
            "imageUrl": "php.png",
            "slug": "php-kursu",
            "date": date(2024, 10, 10),
            "isActive": False,
            "isUpdated": True
        },
        {
            "title": "Java Kursu",
            "description": "Java programlama dili, kolayca aktarılabilir kodu sayesinde platformlar ve cihazlar arasında kullanılır. Java'nın popüler kullanımları arasında kurumsal yazılım, mobil uygulama geliştirme, web uygulamaları, bulut tabanlı uygulamalar, oyunlar ve IoT uygulamaları yer alır.",
            "imageUrl": "java.png",
            "slug": "java-kursu",
            "date": date(2024, 3, 1),
            "isActive": True,
            "isUpdated": True
        },
        {
            "title": "Html Kursu",
            "description": "İngilizce Hyper Text Markup Language cümlesinin baş harflerinden oluşur. İşaretleme dili olan Html, web sayfalarının hazırlanmasında kullanılan sistemdir.",
            "imageUrl": "html.png",
            "slug": "html-kursu",
            "date": date(2024, 7, 7),
            "isActive": False,
            "isUpdated": True
        },
        {
            "title": "Perl Kursu",
            "description": "Perl, bir dil bilimci olup NASA'da sistem yöneticisi olarak çalışan Larry Wall tarafından geliştirilmiş bir programlama dilidir. ",
            "imageUrl": "perl.png",
            "slug": "perl-kursu",
            "date": date(2024, 1, 28),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "C# Kursu",
            "description": "C# yani diğer bir adıyla C Sharp, Microsoft tarafından geliştirilen sunucu ve gömülü sistemleri çalıştırmak için tasarlanmış programlama dilidir.",
            "imageUrl": "csharp.png",
            "slug": "csharp-kursu",
            "date": date(2024, 12, 12),
            "isActive": True,
            "isUpdated": True
        }
    ],
    "categories": [
        {"id": 1, "name": "Programlama", "slug": "programlama"},
        {"id": 2, "name": "Web Geliştirme", "slug": "web-gelistirme"},
        {"id": 3, "name": "Mobil Uygulamalar", "slug": "mobil-uygulamalar"}
    ]
}

def index(request):

    kategoriler = Category.objects.all()

    kurslar = Course.objects.filter(isActive=True)

    return render(request, "courses/index.html", {
        "courses": kurslar,
        "categories": kategoriler
    })

def details(request, slug):
    
    course = get_object_or_404(Course, slug=slug)

    context = {
        "course": course
    }

    return render(request, "courses/details.html", context)

def getCoursesByCategory(request, category_name):

    try:
        category_text = data[category_name]
        return render(request, "courses/courses.html", {
            "category": category_name,
            "category_text": category_text})
    except:
        return HttpResponseNotFound("Yanlış kategori seçimi")

def getCoursesByCategoryId(request, category_id):

    category_list = list(data.keys())

    if category_id > len(category_list) or category_id < 1:
        return HttpResponseNotFound("Yanlış kategori seçimi")
    
    category_name = category_list[category_id - 1]

    redirect_url = reverse("courses_by_category", args=[category_name])

    return redirect(redirect_url)