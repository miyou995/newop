
from django.urls import path
from .views import IndexView, AboutView, ContactView, ServiceCreationDetailView, ServiceGestionView, ServiceSimulationView, ServiceAppelsOffresView
from django.views.generic import TemplateView
urlpatterns = [
    path('', IndexView.as_view(), name='indexView'),
    path('about/', AboutView.as_view(), name='aboutView'),
    path('contact/', ContactView.as_view(), name='contactView'),
    path('creation-entreprise/', ServiceCreationDetailView.as_view(), name='service_creation'),
    path('gestion-entreprise/', ServiceGestionView.as_view(), name='service_gestion'),
    path('simulation-projets/', ServiceSimulationView.as_view(), name='simulation_projets'),
    path('appel-offres-consultations/', ServiceAppelsOffresView.as_view(), name='appel_offres'),
    path('message/', TemplateView.as_view(template_name='success.html'), name='message'),
]
