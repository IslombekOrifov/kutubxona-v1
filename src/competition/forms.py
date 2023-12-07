from django import forms

from import_export.forms import ExportForm

from .models import Competition

class CompetitionParticipantExporForm(ExportForm):
    competition = forms.ModelChoiceField(queryset=Competition.objects.all(),
                                         label='Select Competition',
                                         required=True)