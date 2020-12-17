from django.urls import path

from app.views import all_ListAPIView, Yourself_APIView, level_APIView

urlpatterns = [
    path('', all_ListAPIView.as_view(), name='all_info_about_emploees'),
    path('yourself/', Yourself_APIView.as_view(), name='Yourself_APIView'),
    path('<int:level>', level_APIView.as_view(), name='info_one_level_emploees'),
]
