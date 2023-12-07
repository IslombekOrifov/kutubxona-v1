from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Competition)
class CompetitionTranslationOptions(TranslationOptions):
    fields = ('name',)
    

@register(CompetetionCondition)
class CompetetionConditionTranslationOptions(TranslationOptions):
    fields = ('body',)
    

@register(CompetetionQuestion)
class CompetetionQuestionTranslationOptions(TranslationOptions):
    fields = ('name',)