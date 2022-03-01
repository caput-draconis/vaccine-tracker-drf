import json
from django.core import serializers

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vaccine_drive.models import VaccineDriveDetails
from vaccine_drive.serializers import VaccineDriveSerializer


@api_view(['GET'])
def vaccine_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    serializer =''
    if request.method == 'GET':
        vaccine = VaccineDriveDetails.objects.all()
        serializer = VaccineDriveSerializer(vaccine, many=True)
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def vaccine_update(request,pk):
    if request.method == 'POST':
        vaccine = VaccineDriveDetails.objects.get(pk=pk)
        vaccine.bookedSlots = request.data.get('bookedSlots')
        vaccine.save()
        data = serializers.serialize('json', [vaccine,])
        struct = json.loads(data)
        # data = json.dumps(struct[0])
        return Response(struct[0].get('fields'),status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)