from rest_framework import serializers

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


class all_serializer(serializers.ModelSerializer):
    '''Сериализатор всей информации о сотрудниках'''
    position = Position_relations_serializer(many=True)
    salary_info = Salary_paid_serializer(many=True)
    salary_all = serializers.FloatField()
    class Meta:
        model = Employes
        fields = '__all__'