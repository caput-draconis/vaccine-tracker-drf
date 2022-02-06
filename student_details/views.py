from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student_details.models import StudentDetails
from student_details.serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    # serializer =''
    if request.method == 'GET':
        students = StudentDetails.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
