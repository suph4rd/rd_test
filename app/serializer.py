from rest_framework import serializers
from app.models import Employee, PositionRelations,SalaryPaid


class PositionRelationsSerializer(serializers.ModelSerializer):
    '''Serializer of information about hierarchy'''
    class Meta:
        model = PositionRelations
        fields = '__all__'


class SalaryPaidSerializer(serializers.ModelSerializer):
    '''Serializer of information about salary'''
    class Meta:
        model = SalaryPaid
        fields = '__all__'


class AllSerializer(serializers.ModelSerializer):
    '''Serializer of all information about employee'''
    position = PositionRelationsSerializer()
    salary_info = SalaryPaidSerializer(many=True)
    salary_all = serializers.FloatField()

    class Meta:
        model = Employee
        exclude = ['user',]