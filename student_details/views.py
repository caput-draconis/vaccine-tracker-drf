from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student_details.models import StudentDetails
from student_details.serializers import StudentSerializer


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
    
# changes begin

# class FileUploadView(views.APIView):
#     parser_classes = (FileUploadParser,)

#     def put(self, request, filename, format=None):
#         file_obj = request.FILES['file']
#         # do some stuff with uploaded file
#         return Response(status=204)