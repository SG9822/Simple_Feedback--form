from django.forms import ModelForm, widgets
from .models import *
from django import forms

class FeedbackForm(ModelForm):
    class Meta:
        model = Form
        fields = "__all__"
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'Rate_our_Products_and_services': forms.Select(attrs={'class': 'form-select'}),
            "Give_Your_Valuable_Feedback": forms.Textarea(attrs={'class': 'form-control'})

        }
