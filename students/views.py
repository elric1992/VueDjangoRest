from django.shortcuts import render
from django.http import JsonResponse
from .models import Student


def index(request):
    students = Student.objects.all()
    return JsonResponse(students, safe=False)
