from django.urls import path
from . import views

# http://127.0.0.1:8000/courses                  => kurs listesi
# http://127.0.0.1:8000/courses/listes           => kurs listesi
# http://127.0.0.1:8000/courses/details          => ... detay sayfası


urlpatterns = [
    path("", views.courses),
    path("listes", views.courses),
    path("<course_name>", views.details),
    path("category/<int:category_id>", views.getCourseByCategoryId),
    path("category/<str:category_name>", views.getCourseByCategoryName),
    
]
