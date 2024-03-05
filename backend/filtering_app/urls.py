from django.urls import path
from .views import GetAllData,GetFilteredData,AddNewYelpData,RemoveYelpData

urlpatterns = [
    path('api/GetAllData/',GetAllData.as_view(),name='GetAllData'),
    path('api/GetFilteredData/',GetFilteredData.as_view(),name='GetFilteredData'),
    path('api/AddNewYelpData/',AddNewYelpData.as_view(),name='AddNewYelpData'),
    path('api/RemoveYelpData/<int:pk>',RemoveYelpData.as_view(),name='RemoveYelpData'),
   
]
