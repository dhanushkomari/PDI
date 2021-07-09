from .models import Plant
from django import forms

class upload_form(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ('name','picture',)