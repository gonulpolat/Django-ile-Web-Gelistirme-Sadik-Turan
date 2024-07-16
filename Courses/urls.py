from django.urls import path
from . import views

urlpatterns = [
    path("", views.courses),
    path("liste", views.courses),
    path("<course_name>", views.details),
    path("kategori/<int:category_id>", views.getCoursesByCategoryId),
    path("kategori/<str:category_name>", views.getCoursesByCategory, name="courses_by_category")
]