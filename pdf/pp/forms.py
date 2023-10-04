from django import forms
from .models import pdfs
class pdfForm(forms.ModelForm):
    class Meta:
        model=pdfs
        fields="__all__"