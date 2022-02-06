from django.db import models

# Create your models here.
class VaccineDriveDetails(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=100)
    vaccineName = models.CharField(max_length=100)
    eventDate = models.DateField()
    eventPlace = models.CharField(max_length=100)
    maxSlots = models.IntegerField()
    bookedSlots = models.IntegerField()
