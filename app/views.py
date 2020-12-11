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
        queryset = Employes.objects.filter(position__level=level)
        serializer = all_serializer(queryset, many=True)
        return Response(serializer.data)
