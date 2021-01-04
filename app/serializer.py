from rest_framework import serializers
from app.models import Employee, PositionLevel, SalaryPaid


class PositionLevelSerializer(serializers.ModelSerializer):
    '''Serializer of information about hierarchy'''
    class Meta:
        model = PositionLevel
        fields = '__all__'


class SalaryPaidSerializer(serializers.ModelSerializer):
    '''Serializer of information about salary'''
    class Meta:
        model = SalaryPaid
        fields = '__all__'


class AllSerializer(serializers.ModelSerializer):
    '''Serializer of all information about employee'''
    position = PositionLevelSerializer()
    salary_info = SalaryPaidSerializer(many=True)
    salary_all = serializers.FloatField()

    class Meta:
        model = Employee
        exclude = ['user', ]
