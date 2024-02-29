from rest_framework.response import Response
from rest_framework import generics,pagination
from .models import YelpData
from .serializers import YelpDataSerializer

# class based views handled by djangos rest_framework libraries
# class for basic pagination 

class Pagination(pagination.PageNumberPagination):
    page_size=25
# for paginating data in packets of 25
class GetFilteredData(generics.ListAPIView):
    queryset = YelpData.objects.all()
    serializer_class = YelpDataSerializer
    pagination_class= Pagination
# get all
class GetAllData(generics.ListAPIView):
    queryset = YelpData.objects.all()
    serializer_class = YelpDataSerializer

class AddNewYelpData(generics.CreateAPIView):
    queryset= YelpData.objects.all()
    serializer_class = YelpData
class RemoveYelpData(generics.DestroyAPIView):
    queryset =YelpData.objects.all()
    serializer_class =YelpData
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)