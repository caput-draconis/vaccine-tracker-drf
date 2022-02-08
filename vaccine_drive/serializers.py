from vaccine_drive.models import VaccineDriveDetails
from rest_framework import serializers


class VaccineDriveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VaccineDriveDetails
        fields = ['eventId', 'eventName', 'vaccineName', 'eventDate', 'eventPlace', 'maxSlots', 'bookedSlots']