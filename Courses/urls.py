from django.urls import path
from . import views

urlpatterns = [
    path("", views.courses),
    path("liste", views.courses),
    path("detay", views.details),
    path("<int:category_id>", views.getCoursesByCategoryId),
    path("<str:category_name>", views.getCoursesByCategory)
]