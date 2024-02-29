from rest_framework import serializers
from .models import YelpData

class YelpDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpData
        fields = '__all__'