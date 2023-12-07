from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name', 'sub_name', 'duration', 'description')