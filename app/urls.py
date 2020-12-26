from django.urls import path

from app.views import  LevelAPIView, YourselfAPIView, AllListAPIView

urlpatterns = [
    path('', AllListAPIView.as_view(), name='allInfoAboutEmploees'),
    path('yourself/', YourselfAPIView.as_view(), name='yourselfAPIView'),
    path('<int:level>', LevelAPIView.as_view(), name='infoOneLevelEmploees'),
]
