from rest_framework import serializers
from .models import YelpData

class YelpDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpData
        fields = ['name','address','city','state','stars','review_count','postal_code','categories']
