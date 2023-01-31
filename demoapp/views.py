import serializer as serializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from demoapp.Serializer import StudentSerializer
from demoapp.models import student


# Create your views here.

@api_view(['GET','POST'])
def student_list(request):

    if request.method == 'GET':
        students = student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','DELETE'])
def student_detail(request,id):
    try:
        Students = student.objects.get(id=id)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(Students)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(Students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
