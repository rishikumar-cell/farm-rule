from rest_framework import serializers
from farm.models import Farmer

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'  # Make sure this is a string, not a list or tuple
