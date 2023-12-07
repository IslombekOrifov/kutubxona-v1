from rest_framework import serializers

from .models import (
    Competition, CompetetionCondition, CompetetionQuestion,
    CompetitionParticipant,
)


class CompetetionConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetetionCondition
        exclude = ['is_active', 'created', 'competition']
        

class CompetitionSerializer(serializers.ModelSerializer):
    conditions = CompetetionConditionSerializer(many=True)
    class Meta:
        model = Competition
        fields = ['id', 'name_uz', 'name_ru', 'name_en']


class CompetetionQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetetionQuestion
        fields = ['id', 'name_uz', 'name_ru', 'name_en']
        
        
class CompetitionParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionParticipant
        exclude = ['competition', 'education_is_confirmed', 'education_ball', 
                   'specialty_is_confirmed', 'specialty_ball', 
                   'experience_is_confirmed', 'experience_ball', 
                   'achievement_is_confirmed', 'achievement_ball',
                   'qualification_is_confirmed', 'qualification_ball', 
                   'academ_experience_is_confirmed', 'academ_experience_ball', 
                   'seminar_participation_is_confirmed', 'seminar_participation_ball', 
                   'language_cert_is_confirmed', 'language_cert_ball',
                   'is_active', 'is_confirmed', 'created', 'updated']

