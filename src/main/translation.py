from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title',)
    

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'about', 'description')
    

@register(LeaderAndTrener)
class LeaderAndTrenerTranslationOptions(TranslationOptions):
    fields = ('full_name', 'about')
    

@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)
    

@register(CenterInfo)
class CenterInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'body')
    

@register(CenterStructure)
class CenterStructureTranslationOptions(TranslationOptions):
    fields = ('image',)
    
    
@register(DocumentCategory)
class DocumentCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    

@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('name', 'file')
    
    
@register(Branch)
class BranchTranslationOptions(TranslationOptions):
    fields = ('name', 'about', 'description')
    

@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('name', 'about', 'description')
    