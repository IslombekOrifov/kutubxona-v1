from django.shortcuts import render, get_object_or_404

from rest_framework.generics import (
    GenericAPIView, CreateAPIView
)
from rest_framework import (
    response, status
)

from .models import (
    Competition,
    CompetitionParticipant, 
    CompetetionQuestion
)
from .serializers import (
    CompetitionSerializer,
    CompetitionParticipantSerializer,
    CompetetionQuestionSerializer
)


class CompetitionParticipantCreateAPIView(GenericAPIView):
    queryset = CompetitionParticipant.objects.all()
    serializer_class = CompetitionParticipantSerializer
    
    def post(self, request, *args, **kwargs):
        competition = Competition.objects.filter(is_active=True).last()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(competition=competition)
        return response.Response(status=status.HTTP_201_CREATED)
    
    
class CompetitionQuestionListAPIView(GenericAPIView):
    queryset = CompetetionQuestion.objects.all()
    serializer_class = CompetetionQuestionSerializer
    
    def get(self, request, *args, **kwargs):
        instance = CompetetionQuestion.objects.filter(is_active=True)
        education = instance.filter(education=True)
        experience = instance.filter(experience=True)
        specialty = instance.filter(specialty=True)
        achievement = instance.filter(achievement=True)
        qualification = instance.filter(qualification=True)
        academ_experience = instance.filter(academ_experience=True)
        seminar_participation = instance.filter(seminar_participation=True)
        
        education_serializers = CompetetionQuestionSerializer(education, many=True)
        experience_serializers = CompetetionQuestionSerializer(experience, many=True)
        specialty_serializers = CompetetionQuestionSerializer(specialty, many=True)
        achievement_serializers = CompetetionQuestionSerializer(achievement, many=True)
        qualification_serializers = CompetetionQuestionSerializer(qualification, many=True)
        academ_experience_serializers = CompetetionQuestionSerializer(academ_experience, many=True)
        seminar_participation_serializers = CompetetionQuestionSerializer(seminar_participation, many=True)
        
        
        return response.Response({'education': education_serializers.data,
                                  'experience': experience_serializers.data,
                                  'specialty': specialty_serializers.data,
                                  'achievement': achievement_serializers.data,
                                  'qualification': qualification_serializers.data,
                                  'academ_experience': academ_experience_serializers.data,
                                  'seminar_participation': seminar_participation_serializers.data})


class CompetitionRetriveAPIView(GenericAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    
    def get(self, request, *args, **kwargs):
        datas = self.get_queryset()
        instance = self.get_serializer(data=datas, many=True)
        instance.is_valid()
        return response.Response(instance.data)