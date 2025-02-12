from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FarmerSerializer
from farm.models import Farmer



# Create your views here.
@api_view(['GET'])
def get_farmer_data(request):
    farmers=Farmer.objects.all()
    serializer=FarmerSerializer(farmers,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def add_farmer_data(request):
    serializer=FarmerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    

