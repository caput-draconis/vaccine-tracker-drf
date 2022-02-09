from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student_details.models import StudentDetails
from student_details.serializers import StudentSerializer
from student_details.serializers import FileUploadSerializer


@api_view(['GET'])
def student_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    serializer =''
    if request.method == 'GET':
        students = StudentDetails.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def student_add(request):
    serializer =''
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def student_delete(request, pk):
    if request.method == 'DELETE':
        student = StudentDetails.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class BulkAdd(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = StudentDetails(
                       studentName= row['studentName'],
                       studentClass= row['studentClass'],
                       studentContact= row['studentContact'],
                       studentGender= row['studentGender'],
                       studentDOB= row['studentDOB'],
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)