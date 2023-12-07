from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')