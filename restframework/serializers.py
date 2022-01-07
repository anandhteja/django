from rest_framework import serializers
from admissions.models import Student


class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'