from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name="course_details"),
    path('kategori/<int:category_id>', views.getCoursesById),
    path('kategori/<str:category_name>', views.getCoursesByCategory, name="courses_by_category")
    
]
