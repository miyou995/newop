from django.forms import ModelForm, fields
from .models import Meeting
from django import forms

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields='__all__'

def must_be_empty(value):
    if value:
        raise forms.ValidationError('ce champs doit etre vide')

class ContactForm(forms.Form):
    name = forms.CharField(required = True, max_length=150) 
    email = forms.CharField(max_length=254)
    phone = forms.CharField(max_length=25)
    subject = forms.CharField(max_length=300) 
    honeypot = forms.CharField(required=False,  label="leave empty", validators=[must_be_empty])
    message = forms.CharField()    

