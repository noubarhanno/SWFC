from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from Registration.forms import RegistrationForm
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class CreateRegistration(CreateView):
    # fields = ('First_Name','Last_Name','Email_Address','Mobile_Number','Intereset')
    #fields above has fixed types and variable names should look on internet about it
    form_class=RegistrationForm
    model=models.Registration
    #we have to tell the Template Name which will be used for registration
    template_name='sharjah_waterfront_city/index.html'

class IndexView(TemplateView):
    template_name='sharjah_waterfront_city/successful.html'

class RegistrationList(LoginRequiredMixin,ListView):
    # # login_url='/login/'
    # # redirect_field_name='Registration_Azizi/Registration_Details.html'
    # # template_name="Registration_Azizi/Registration_Details.html"
    # # context_object_name='RegistrationList'
    # # model = models.Registration
    # login_url='/login/'
    # redirect_field_name='Registration_Azizi/registration-list.html'
    # context_object_name='RegistrationList'
    # # template_name="Registration_Azizi/Registration_Details.html"
    # model=models.Registration
    template_name='sharjah_waterfront_city/registration_list.html'
    context_object_name='RegistrationList'
    def get_queryset(self):
        return models.Registration.objects.order_by('-First_Name')
