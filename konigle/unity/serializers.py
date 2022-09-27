import imp
from rest_framework import serializers
from .models import UnityEmail


class UnityEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnityEmail
        fields = '__all__'

    def create(self, validated_data):
        return UnityEmail.objects.create(**validated_data)
