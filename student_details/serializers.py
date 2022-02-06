from student_details.models import StudentDetails
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ['studentId', 'studentName', 'studentClass','studentContact', 'studentGender','studentDOB']