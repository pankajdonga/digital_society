from django import forms
from .models import *

class InvoiceForm(forms.ModelForm):
    class Meta:
        model=invoice
        fields='__all__'

class AddEventForm(forms.ModelForm):
    class Meta:
        model=AddEvent
        fields='__all__'
