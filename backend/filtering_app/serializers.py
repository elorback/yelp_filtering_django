from rest_framework import serializers
from .models import YelpData

class YelpDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpData
        fields = ['name','city','state','stars','review_count','postal_code']
class StarAndStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpData
        fields =['state','stars']