from rest_framework.response import Response
from rest_framework import generics,pagination
from .models import YelpData
from .serializers import YelpDataSerializer,StarAndStateSerializer

# class based views handled by djangos rest_framework libraries
# class for basic pagination 

class Pagination(pagination.PageNumberPagination):
    page_size=25
# for paginating data in packets of 25

class GetStateAndStarList(generics.ListAPIView):
    serializer_class = StarAndStateSerializer

    def get_queryset(self):
        unique_stars = list(YelpData.objects.values_list('stars', flat=True).distinct())
        unique_state = list(YelpData.objects.values_list('state', flat=True).distinct())
        
        # Create a dictionary with 'stars' and 'state' as keys
        result = {'state': unique_state,'stars': unique_stars}
        
        print(result)
        return Response(result)
    
class GetFilteredData(generics.ListAPIView):
    queryset = YelpData.objects.all()
    serializer_class = YelpDataSerializer
    pagination_class= Pagination
    def get_queryset(self):
        queryset = YelpData.objects.all()
        name = self.request.query_params.get('name',None)
        city = self.request.query_params.get('city',None)
        state = self.request.query_params.get('state',None)
        stars = self.request.query_params.get('stars',None)
        review_count = self.request.query_params.get('review_count',None)
        postal_code = self.request.query_params.get('postal_code',None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if city:
            queryset = queryset.filter(city__icontains=city)
        if state:
            queryset = queryset.filter(state__icontains=state)
        if stars:
            queryset = queryset.filter(stars__icontains=stars)
        if review_count:
            queryset = queryset.filter(review_count__icontains=review_count)
        if postal_code:
            queryset = queryset.filter(postal_code__icontains=postal_code)
        print(queryset)
        return queryset
            

        
        

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