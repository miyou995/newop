
from opapp.models import Meeting
from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.utils.translation import gettext as _ 
from django.utils.translation import activate, get_language, gettext
from .models import Meeting
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class ServiceCreationDetailView(CreateView):
    model = Meeting
    fields = '__all__'
    success_url = reverse_lazy('message')
    template_name = "service-creation-entreprise.html"

class ServiceGestionView(CreateView):
    model = Meeting
    fields = '__all__'
    success_url = reverse_lazy('message')
    template_name = "service-gestion-entreprise.html"

class ServiceSimulationView(CreateView):
    model = Meeting
    fields = '__all__'
    success_url = reverse_lazy('message')
    template_name = "service-simulation.html"

class ServiceAppelsOffresView(CreateView):
    model = Meeting
    fields = '__all__'
    success_url = reverse_lazy('message')
    template_name = "service-appels-offres.html"


    