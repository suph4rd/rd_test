from rest_framework import serializers
from rest_framework_simplejwt.state import User
from app.models import Employes, Position_relations, Salary_paid


class Position_relations_serializer(serializers.ModelSerializer):
    '''Сериализатор информации о иерархии должностей'''
    class Meta:
        model = Position_relations
        fields = '__all__'


class Salary_paid_serializer(serializers.ModelSerializer):
    '''Сериализатор информации о заработной плате'''
    class Meta:
        model = Salary_paid
        fields = '__all__'

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class all_serializer(serializers.ModelSerializer):
    '''Сериализатор всей информации о сотрудниках'''
    position = Position_relations_serializer()
    salary_info = Salary_paid_serializer(many=True)
    salary_all = serializers.FloatField()
    user = User_serializer()
    class Meta:
        model = Employes
        fields = '__all__'