from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    studentId = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=100)
    studentClass = models.IntegerField()
    studentContact = models.BigIntegerField()
    studentGender = models.CharField(max_length=1)
    studentDOB = models.DateField()