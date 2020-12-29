from rest_framework import serializers
from app.models import Employee, PositionRelations,SalaryPaid


class Position_relations_serializer(serializers.ModelSerializer):
    '''Serializer of information about hierarchy'''
    class Meta:
        model = PositionRelations
        fields = '__all__'


class Salary_paid_serializer(serializers.ModelSerializer):
    '''Serializer of information about salary'''
    class Meta:
        model = SalaryPaid
        fields = '__all__'


class all_serializer(serializers.ModelSerializer):
    '''Serializer of all information about employee'''
    position = Position_relations_serializer()
    salary_info = Salary_paid_serializer(many=True)
    salary_all = serializers.FloatField()
    class Meta:
        model = Employee
        exclude = ['user',]