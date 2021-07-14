from django.db import models
from django.urls import reverse

# Create your models here.
class Meeting(models.Model):
    name = models.CharField(verbose_name='Nom', max_length=150) 
    email = models.EmailField(max_length=254,blank=True, null=True)
    phone = models.CharField(max_length=25,blank=True, null=True)
    subject = models.CharField(max_length=300,blank=True, null=True) 
    day = models.DateField(blank=True, null=True)
    hour = models.TimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    # def get_absolute_url(self):
    #     return reverse("indexView", kwargs={"pk": self.pk})
    