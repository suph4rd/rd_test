from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Employee
from app.serializer import all_serializer


class AllListAPIView(ListAPIView):
    '''All information about employees'''
    queryset = Employee.objects.defer('user') \
                                .select_related('position') \
                                .prefetch_related('salarypaid_set')
    serializer_class = all_serializer
    permission_classes = (permissions.IsAdminUser,)


class LevelAPIView(APIView):
    '''Information about employees by level'''
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, level):
        queryset = Employee.objects.filter(position__level=level) \
                                    .defer('user') \
                                    .select_related('position')\
                                    .prefetch_related('salarypaid_set')
        serializer = all_serializer(queryset, many=True)
        return Response(serializer.data)


class YourselfAPIView(APIView):
    '''Information about yourself'''
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        queryset = Employee.objects.select_related('position') \
                                    .prefetch_related('salarypaid_set')\
                                    .get(user__id=request.user.id)
        serializer = all_serializer(queryset)
        return Response(serializer.data)