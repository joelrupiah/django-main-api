from tabnanny import verbose
from django.db import models

# Create your models here.

# TEACHER MODEL

class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile=models.CharField(max_length=20)
    skills=models.TextField()

# COURSE CATEGORY MODEL

class CourseCategory(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()

    # modification of this model
    class Meta:
        verbose_name_plural="Course Categories" # changes from course categorys to course categories

# COURSE MODEL

class Course(models.Model):
    category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()

# STUDENT MODEL

class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile=models.CharField(max_length=20)
    address=models.TextField()
    interested_categories=models.TextField()