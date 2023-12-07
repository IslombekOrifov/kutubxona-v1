from django.db import models

# from main.models import Region

from .services import upload_participant_path


EDUCATION_CHOICE = (
    (0, 0),
    (2, 2),
    (5, 5),
    (10, 10),
)

SPECIALTY_CHOICE = (
    (0, 0),
    (6, 6),
    (8, 8),
    (10, 10),
)

EXPERIENCE_CHOICE = (
    (0, 0),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)

ACHIEVEMENT_CHOICE = (
    (0, 0),
    (2, 2),
    (3, 3),
    (5, 5),
    (7, 7),
    (10, 10),
)

QUALIFICATION_CHOICE = (
    (0, 0),
    (5, 5),
    (8, 8),
    (10, 10),
)

ACADEMIC_EXPERIENCE_CHOICE = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (6, 6),
    (10, 10),
    (14, 14),
    (18, 18),
)

SEMINAR_PARTICIPANT_CHOICE = (
    (0, 0),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (10, 10),
)

LANGUAGE_CHOICE = (
    (0, 0),
    (7, 7),
    (10, 10),
    (14, 14),
    (18, 18),
)


class Competition(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class CompetetionCondition(models.Model):
    body = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    competition = models.ForeignKey(Competition,
                                    on_delete=models.CASCADE,
                                    related_name='conditions')
        
        
class CompetetionQuestion(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    education = models.BooleanField(default=False)
    experience = models.BooleanField(default=False)
    specialty = models.BooleanField(default=False)
    achievement = models.BooleanField(default=False)
    qualification = models.BooleanField(default=False)
    academ_experience = models.BooleanField(default=False)
    seminar_participation = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class CompetitionParticipant(models.Model):
    competition = models.ForeignKey(Competition,
                                    on_delete=models.CASCADE,
                                    related_name='participants')
    full_name = models.CharField(max_length=100)
    region = models.ForeignKey('main.Region',
                               on_delete=models.PROTECT,
                               related_name='participants')
    phone = models.CharField(max_length=16)
    work_place = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    
    
    education = models.ForeignKey(CompetetionQuestion,
                                  on_delete=models.PROTECT,
                                  related_name='education_participants',
                                  blank=True,
                                  null=True)
    education_file = models.FileField(upload_to=upload_participant_path, blank=True, null=True)
    education_is_confirmed = models.BooleanField(default=False, blank=True)
    education_ball = models.SmallIntegerField(choices=EDUCATION_CHOICE, blank=True, default=0)
    
    specialty = models.ForeignKey(CompetetionQuestion,
                                  on_delete=models.PROTECT,
                                  related_name='specialty_participants',
                                  blank=True,
                                  null=True)
    specialty_file = models.FileField(upload_to=upload_participant_path, blank=True, null=True)
    specialty_is_confirmed = models.BooleanField(default=False, blank=True)
    specialty_ball = models.SmallIntegerField(choices=SPECIALTY_CHOICE, blank=True, default=0)
    
    experience = models.ForeignKey(CompetetionQuestion,
                                   on_delete=models.PROTECT,
                                   related_name='experience_participants',
                                   blank=True,
                                   null=True)
    experience_file = models.FileField(upload_to=upload_participant_path, blank=True, null=True)
    experience_is_confirmed = models.BooleanField(default=False, blank=True)
    experience_ball = models.SmallIntegerField(choices=EXPERIENCE_CHOICE, blank=True, default=0)
    
    achievement = models.ForeignKey(CompetetionQuestion,
                                    on_delete=models.PROTECT,
                                    related_name='achievement_participants',
                                    blank=True,
                                    null=True)
    achievement_file = models.FileField(upload_to=upload_participant_path, blank=True, null=True)
    achievement_is_confirmed = models.BooleanField(default=False, blank=True)
    achievement_ball = models.SmallIntegerField(choices=ACHIEVEMENT_CHOICE, blank=True, default=0)
    
    qualification = models.ForeignKey(CompetetionQuestion,
                                      on_delete=models.PROTECT,
                                      related_name='qualification_participants',
                                      blank=True,
                                      null=True)
    qualification_file = models.FileField(upload_to=upload_participant_path, blank=True, null=True)
    qualification_is_confirmed = models.BooleanField(default=False, blank=True)
    qualification_ball = models.SmallIntegerField(choices=QUALIFICATION_CHOICE, blank=True, default=0)
    
    academ_experience = models.ForeignKey(CompetetionQuestion,
                                    on_delete=models.PROTECT,
                                    related_name='academ_participants',
                                    blank=True,
                                    null=True)
    academ_experience_file = models.FileField(upload_to=upload_participant_path, blank=True, null=True)
    academ_experience_is_confirmed = models.BooleanField(default=False, blank=True)
    academ_experience_ball = models.SmallIntegerField(choices=ACADEMIC_EXPERIENCE_CHOICE,
                                                      blank=True, default=0)
    seminar_participation = models.ForeignKey(CompetetionQuestion,
                                    on_delete=models.PROTECT,
                                    related_name='seminar_participants',
                                    blank=True,
                                    null=True)
    seminar_participation_file = models.FileField(upload_to=upload_participant_path, blank=True, null=True)
    seminar_participation_is_confirmed = models.BooleanField(default=False, blank=True)
    seminar_participation_ball = models.SmallIntegerField(choices=SEMINAR_PARTICIPANT_CHOICE,
                                                          blank=True, default=0)
    
    language_cert = models.CharField(max_length=5, blank=True, null=True)
    language_cert_file = models.FileField(upload_to=upload_participant_path, blank=True, null=True)
    language_cert_is_confirmed = models.BooleanField(default=False, blank=True)
    language_cert_ball = models.SmallIntegerField(choices=LANGUAGE_CHOICE, blank=True, default=0)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']

    
    

