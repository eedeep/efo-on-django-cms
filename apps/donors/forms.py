from django import forms
from django.db.models import get_model

class DonorAdminModelForm(forms.ModelForm):
    
    class Meta:
        model = get_model('donors', 'donor')
