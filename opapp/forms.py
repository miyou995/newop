from django.forms import ModelForm, fields
from .models import Meeting

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields='__all__'