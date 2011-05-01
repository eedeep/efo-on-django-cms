from django import forms
from django.db.models import get_model

class ProgrammeAdminModelForm(forms.ModelForm):
    
    class Meta:
        model = get_model('programmes', 'programme')
        widgets = {
            'needs': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
            'objectives': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
            'activities': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
            'long_term_impact': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
            'funding_info': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
            'how_to_help': forms.Textarea(
                attrs={ 'class': 'mceEditor', }),
        }
