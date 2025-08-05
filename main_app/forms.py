from django import forms
from .models import Feeding
# https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/#modelform
class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }