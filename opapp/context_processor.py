from .models import Meeting
from .forms import MeetingForm
from django.template import RequestContext
from django.shortcuts import render
from django.urls import reverse_lazy



def meeting_form(request):
    return {'form': MeetingForm() }