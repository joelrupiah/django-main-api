from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
# from rest_framework.views import APIView
from .serializers import TeacherSerializer, CategorySerializer, CourseSerializer
# from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from . import models

# Create your views here.

# class TeacherList(APIView):
#     def get(self, request):
#         teachers=models.Teacher.objects.all()
#         serializer=TeacherSerializer(teachers, many=True)
#         return Response(serializer.data)

class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def teacher_login(request):
    email = request.POST['email']
    password = request.POST['password']

    teacherData = models.Teacher.objects.get(email=email, password=password)

    if teacherData:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})

class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer

class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer