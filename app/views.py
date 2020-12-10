from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Employes
from app.serializer import all_serializer


class all_ListAPIView(ListAPIView):
    '''Вся информация о сотрудниках'''
    queryset = Employes.objects.all()
    serializer_class = all_serializer


class level_APIView(APIView):
    '''Информация о сотрудниках по уровням'''
    def get(self, request, level):
        print(level)
        queryset = Employes.objects.filter(position__level=level)
        for x in queryset:
            print(x)
        print(queryset)
        # return Response(queryset)
        serializer = all_serializer(queryset, many=True)
        print(serializer)
        return Response(serializer.data)
