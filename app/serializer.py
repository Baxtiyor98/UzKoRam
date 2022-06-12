from rest_framework import serializers
from .models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class MurojatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Murojat
        fields = '__all__'

class YuridikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yuridik
        fields = '__all__'