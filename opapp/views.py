
from django import forms
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.utils.translation import gettext as _ 
from django.utils.translation import activate, get_language, gettext
from .models import Meeting
from django.urls import reverse_lazy
from .forms import ContactForm, MeetingForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.contrib import messages
from django.views.generic.edit import FormView



def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            print('JSYOUIIII')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            day = form.cleaned_data['day']
            hour = form.cleaned_data['hour']
            message = form.cleaned_data['message']

            meeting = Meeting.objects.create(
                name = name,
                email = email,
                phone = phone,
                subject = subject,
                day = day,
                hour = hour,
                message = message
            )
            meeting.save()
            return redirect('/message')
            
 


class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"


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


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('message')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = ['contact@newoppportunitygc.com']
            body = 'Nom: {} \n email: {} \n Phone:{} \n Sujet: {} \n Message: {}' .format(name, email, phone, subject, message)
            mail = EmailMessage('Cet email est envoyer depuis le site internet', body, 'inter.taki@gmail.com', ['inter-95@hotmail.fr']) 
            print('JE SUIS LAAAAAAAAAAAAAAAAAAAAAAAA')
            try:
                mail.send()
                return redirect('/message')
            except:
                return redirect('/')
