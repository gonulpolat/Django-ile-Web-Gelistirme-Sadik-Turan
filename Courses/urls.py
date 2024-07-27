from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create-course", views.createCourse, name="create_course"),
    path("course-list", views.courseList, name="course_list"),
    path("course-edit/<int:id>", views.courseEdit, name="course_edit"),
    path("<slug:slug>", views.details, name="course_details"),
    path("kategori/<slug:slug>", views.getCoursesByCategory, name="courses_by_category")
]