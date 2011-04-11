from django import forms
from django.db.models import get_model

class ProgrammeAdminModelForm(forms.ModelForm):
    
    class Meta:
        model = get_model('programmes', 'programme')
