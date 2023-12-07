from django.shortcuts import render, get_object_or_404

from rest_framework.generics import (
    GenericAPIView, CreateAPIView
)
from rest_framework import (
    response, status
)

from .models import Course
from .serializers import (
    CourseSerializer, CourseListSerializer,
    CourseApplicationSerializer,
)


class OnlineCoursesAPIView(GenericAPIView):
    queryset = Course.objects.filter(is_online=True, is_active=True)
    serializer_class = CourseListSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class OfflineCoursesAPIView(GenericAPIView):
    queryset = Course.objects.filter(is_online=False, is_active=True)
    serializer_class = CourseListSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
    

class CourseDetailAPIView(GenericAPIView):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer
    
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=kwargs['pk'])
        if not instance:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)
    

class CourseApplicationCreateAPIView(GenericAPIView):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer
    
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'], is_active=True)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(course=course)
        return response.Response(status=status.HTTP_201_CREATED)