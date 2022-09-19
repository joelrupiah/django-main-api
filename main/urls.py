from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login', views.teacher_login),

    # Category
    path('categories/', views.CategoryList.as_view()),

    # Course
    path('course/', views.CourseList.as_view()),
]