from dataclasses import fields
from rest_framework import serializers
from base.models import StudentData


class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = '__all__'
