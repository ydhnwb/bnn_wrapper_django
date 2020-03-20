from rest_framework import serializers
from .models import *

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'

class ProvinceSerializer(serializers.Serializer):
    province_name = serializers.CharField()
    url = serializers.CharField()