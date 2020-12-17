from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Employes
from app.serializer import all_serializer


class all_ListAPIView(ListAPIView):
    '''Вся информация о сотрудниках'''
    queryset = Employes.objects.select_related('position')\
                                .all()\
                                .defer('user')
    serializer_class = all_serializer
    permission_classes = (permissions.IsAdminUser,)


class level_APIView(APIView):
    '''Информация о сотрудниках по уровням'''
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, level):
        print(request.headers)
        queryset = Employes.objects.select_related('position')\
                                    .filter(position__level=level)\
                                    .defer('user')
        serializer = all_serializer(queryset, many=True)
        return Response(serializer.data)


class Yourself_APIView(APIView):
    '''Информация о себе'''
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        queryset = Employes.objects.select_related('position') \
                                    .defer('user')\
                                    .get(user__id=request.user.id)
        serializer = all_serializer(queryset)
        return Response(serializer.data)
