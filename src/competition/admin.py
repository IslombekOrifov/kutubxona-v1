from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ExportMixin


from .models import (
    Competition, CompetetionCondition, CompetetionQuestion,
    CompetitionParticipant
)
from .forms import CompetitionParticipantExporForm


@admin.register(Competition)
class CompetitionAdmin(TranslationAdmin):
    list_display = ('name', 'is_active', 'created', 'updated')
    list_filter = ('created', 'updated')
    ordering = ('is_active', 'created', 'updated')
    # fieldsets = (
    #     ('Translateble', {
    #       'fields': ('name',)
    #     }),
    #     ('Standard info', {
    #         'fields': ('is_active',)
    #     }),
      
    # )

    

@admin.register(CompetetionCondition)
class CompetetionConditionAdmin(TranslationAdmin):
    list_display = ('body', 'competition', 'is_active', 'created')
    list_filter = ('created',)
    ordering = ('is_active', 'created', 'competition')
    fieldsets = (
        ('Translateble', {
          'fields': ('body',)
        }),
        ('Standard info', {
            'fields': ('is_active',)
        }),
      
    )

@admin.register(CompetetionQuestion)
class CompetetionQuestionAdmin(TranslationAdmin):
    list_display = (
        'name', 'is_active', 'education', 'experience', 'specialty',
        'achievement', 'qualification', 'academ_experience',
        'seminar_participation', 'created'
    )
    list_filter = ('created',)
    ordering = ('is_active', 'education', 'experience', 'specialty',
        'achievement', 'qualification', 'academ_experience',
        'seminar_participation', 'created'
    )
    fieldsets = (
        ('Translateble', {
          'fields': ('name',)
        }),
        ('Standard info', {
            'fields': ('is_active', ('education', 'experience'),
                       ('specialty', 'achievement'), ('qualification', 'academ_experience'), 'seminar_participation')
        }),
      
    )


class CompetitionParticipantResource(resources.ModelResource):
    competition = fields.Field(
        column_name='competition',
        attribute='competition',
        widget=ForeignKeyWidget(Competition, 'name_uz')
    )
    
    region = fields.Field(
        column_name='region',
        attribute='region',
        widget=ForeignKeyWidget('main.Region', 'name_uz')
    )
    
    def __init__(self, **kwargs):
        super().__init__()
        self.competition_id = kwargs.get("competition_id") 
        
        
    def filter_export(self, queryset, *args, **kwargs):
        return queryset.filter(competition_id=self.competition_id)

    class Meta:
        model = CompetitionParticipant
        fields = ('competition', 'full_name', 'region', 'phone', 'work_place', 'is_confirmed')
        export_order = fields


@admin.register(CompetitionParticipant)
class CompetitionParticipantAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('full_name', 'competition', 'region', 'phone', 'is_active', 'is_confirmed', 'created', 'updated')
    list_filter = ('created', 'updated', 'is_active', 'is_confirmed', 'region')
    # raw_id_fields = ['education', 'specialty', 'experience', 'achievement', 'qualification', 'academ_experience', 'seminar_participation',]
    ordering = ('-created', 'is_active', 'is_confirmed', 'competition', 'updated')
    actions = ['export_selected'] 
    resource_class = CompetitionParticipantResource
    export_form_class = CompetitionParticipantExporForm

    def get_export_resource_kwargs(self, request, *args, **kwargs):
        export_form = kwargs["export_form"]
        if export_form:
            return dict(competition_id=export_form.cleaned_data["competition"].id)
        return {}