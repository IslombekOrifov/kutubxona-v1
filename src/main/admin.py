from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (
    Slider, News, Result, LeaderAndTrener, Partner, 
    UserContact, CenterSocial, CenterInfo, DocumentCategory, Document,
    Branch, Region, CenterContact, CenterStructure, Event, EventImages
)


@admin.register(Slider)
class SliderAdmin(TranslationAdmin):
    list_display = ('title', 'image', 'url', 'is_active', 'created')
    list_filter = ('created',)
    ordering = ('is_active', 'created')
    fieldsets = (
        ('Translateble', {
          'fields': ('title',)
        }),
        ('Standard info', {
            'fields': ('image', 'url', 'is_active')
        }),
      
    )
    

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('name', 'is_active', 'is_news', 'created')
    list_filter = ('created',)
    ordering = ('is_news', 'is_active', 'created')
    fieldsets = (
        ('Translateble', {
          'fields': ('name', 'about', 'description')
        }),
        ('Standard info', {
            'fields': ('image', 'is_active', 'is_news')
        }),
      
    )
    
@admin.register(Result)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('online', 'offline')
    

@admin.register(LeaderAndTrener)
class LeaderAndTrenerAdmin(TranslationAdmin):
    list_display = ('full_name', 'is_leader',)
    fieldsets = (
        ('Translateble', {
          'fields': ('full_name', 'about')
        }),
        ('Standard info', {
            'fields': ('image', 'is_leader', 'work_time', 'phone',
                       'email', 'telegram', 'instagram', 'facebook')
        }),
      
    )
    
    
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'url', 'is_active')
    ordering = ('is_active',)


@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'academic_degree',)
    list_filter = ('created',)
    ordering = ('academic_degree', 'created')


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = ('id', 'name',)

    
@admin.register(CenterContact)
class CenterContactAdmin(admin.ModelAdmin):
    list_display = ('tel', 'address')
    

@admin.register(CenterSocial)
class CenterSocialAdmin(admin.ModelAdmin):
    list_display = ('center', 'name', 'code', 'url')
    
    
@admin.register(CenterInfo)
class CenterInfoAdmin(TranslationAdmin):
    list_display = ('title', 'subtitle', 'file', 'is_history')
    fieldsets = (
        ('Translateble', {
          'fields': ('title', 'subtitle', 'body')
        }),
        ('Standard info', {
            'fields': ('file', 'is_history')
        }),
      
    )    
    

@admin.register(CenterStructure)
class CenterStructureAdmin(TranslationAdmin):
    list_display = ('image',)
    
    
@admin.register(DocumentCategory)
class DocumentCategoryAdmin(TranslationAdmin):
    list_display = ('name',)
     
    
@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    list_display = ('name', 'file', 'url', 'category',)
    fieldsets = (
        ('Translateble', {
          'fields': ('name', 'file')
        }),
        ('Standard info', {
            'fields': ('url', 'category')
        }),
    )   
 
 
@admin.register(Branch)
class BranchAdmin(TranslationAdmin):
    list_display = ('name', 'image', 'site', 'region',)
    ordering = ('region',)
    fieldsets = (
        ('Translateble', {
          'fields': ('name', 'about', 'description')
        }),
        ('Standard info', {
            'fields': ('image', 'site', 'region')
        }),
    )   
    

class EventImagesAdmin(admin.TabularInline):
    model = EventImages
    raw_id_fields = ['event']
    

@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ('name', 'image', 'is_active', 'created')
    ordering = ('created', 'is_active')
    fieldsets = (
        ('Translateble', {
          'fields': ('name', 'description', 'about')
        }),
        ('Standard info', {
            'fields': ('image', 'is_active')
        }),
    ) 
    inlines = [EventImagesAdmin]
    


