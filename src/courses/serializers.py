from rest_framework import serializers

from .models import (
    Course, CourseApplication
)


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['description', 'is_online', 'is_active', 'created']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['is_online', 'is_active', 'created']
        

class CourseApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseApplication
        exclude = ['is_checked', 'created']
        extra_kwargs = {
            'id': {'read_only': True, 'required': False},
            'course': {'read_only': True, 'required': False},
        }