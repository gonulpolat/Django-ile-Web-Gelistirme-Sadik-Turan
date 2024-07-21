from datetime import date
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

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
            "imageUrl": "https://randomwordgenerator.com/img/picture-generator/57e6d0434253b10ff3d8992cc12c30771037dbf852547941762a7fdc974c_640.jpg",
            "slug": "javascript-kursu",
            "date": date(2024, 1, 16),
            "isActive": True
        },
        {
            "title": "Python Kursu",
            "description": "Python; web uygulamaları, yazılım geliştirme, veri bilimi ve makine öğreniminde (ML) yaygın olarak kullanılan bir programlama dilidir. Geliştiriciler, etkili ve öğrenmesi kolay olduğu ve birçok farklı platformda çalıştırılabildiği için Python'ı kullanır.",
            "imageUrl": "https://randomwordgenerator.com/img/picture-generator/54e4d14b4f56ad14f1dc8460962e33791c3ad6e04e507440752f78d09548c4_640.jpg",
            "slug": "python-kursu",
            "date": date(2024, 4, 26),
            "isActive": True
        },
        {
            "title": "Php Kursu",
            "description": "PHP (Hypertext Preprocessor), yaygın olarak kullanılan web tabanlı ve açık kaynak kodlu bir programlama dilidir.",
            "imageUrl": "https://randomwordgenerator.com/img/picture-generator/54e5d3464357ab14f1dc8460962e33791c3ad6e04e50744172297cd59645c1_640.jpg",
            "slug": "php-kursu",
            "date": date(2024, 10, 10),
            "isActive": False
        },
        {
            "title": "Java Kursu",
            "description": "Java programlama dili, kolayca aktarılabilir kodu sayesinde platformlar ve cihazlar arasında kullanılır. Java'nın popüler kullanımları arasında kurumsal yazılım, mobil uygulama geliştirme, web uygulamaları, bulut tabanlı uygulamalar, oyunlar ve IoT uygulamaları yer alır.",
            "imageUrl": "https://randomwordgenerator.com/img/picture-generator/54e9d1454b5ba914f1dc8460962e33791c3ad6e04e507440752b7edc9649c2_640.jpg",
            "slug": "java-kursu",
            "date": date(2024, 3, 1),
            "isActive": True
        },
        {
            "title": "Html Kursu",
            "description": "İngilizce Hyper Text Markup Language cümlesinin baş harflerinden oluşur. İşaretleme dili olan Html, web sayfalarının hazırlanmasında kullanılan sistemdir.",
            "imageUrl": "https://randomwordgenerator.com/img/picture-generator/57e4d1474e5ba914f1dc8460962e33791c3ad6e04e5074417d2f7dd49f4ec6_640.jpg",
            "slug": "html-kursu",
            "date": date(2024, 7, 7),
            "isActive": False
        },
        {
            "title": "Perl Kursu",
            "description": "Perl, bir dil bilimci olup NASA'da sistem yöneticisi olarak çalışan Larry Wall tarafından geliştirilmiş bir programlama dilidir. ",
            "imageUrl": "https://randomwordgenerator.com/img/picture-generator/52e1d64a435aae14f1dc8460962e33791c3ad6e04e507441722a72dd904ac1_640.jpg",
            "slug": "perl-kursu",
            "date": date(2024, 1, 28),
            "isActive": True
        },
        {
            "title": "C# Kursu",
            "description": "C# yani diğer bir adıyla C Sharp, Microsoft tarafından geliştirilen sunucu ve gömülü sistemleri çalıştırmak için tasarlanmış programlama dilidir.",
            "imageUrl": "https://randomwordgenerator.com/img/picture-generator/5fe5d5434f4faa0df7c5d57bc32f3e7b1d3ac3e455517349772672d595_640.jpg",
            "slug": "csharp-kursu",
            "date": date(2024, 12, 12),
            "isActive": True
        }
    ],
    "categories": [
        {"id": 1, "name": "Programlama", "slug": "programlama"},
        {"id": 2, "name": "Web Geliştirme", "slug": "web-gelistirme"},
        {"id": 3, "name": "Mobil Uygulamalar", "slug": "mobil-uygulamalar"}
    ]
}

def index(request):

    kategoriler = db["categories"]

    # list comprehension
    kurslar = [course for course in db["courses"] if course["isActive"]]

    return render(request, "courses/index.html", {
        "courses": kurslar,
        "categories": kategoriler
    })

def details(request, course_name):
    return HttpResponse(f"{course_name} detay sayfası")

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