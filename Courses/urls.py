from django.urls import path
from . import views

# http://127.0.0.1:8000/courses         => kurs listesi
# http://127.0.0.1:8000/client/courses  => kurs listesi


urlpatterns = [
    path("courses", views.courses),
]
