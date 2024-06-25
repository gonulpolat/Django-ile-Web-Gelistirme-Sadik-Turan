from django.urls import path
from . import views

# http://127.0.0.1:8000/courses                  => kurs listesi
# http://127.0.0.1:8000/courses/listes           => kurs listesi
# http://127.0.0.1:8000/courses/details          => kurs detay sayfası


urlpatterns = [
    path("", views.courses),
    path("listes", views.courses),
    path("details", views.details),
    path("<int:category_id>", views.getCourseByCategoryId),
    path("<str:category_name>", views.getCourseByCategoryName),
    
]
