from django.conf.urls import url,include
from Registration.views import RegistrationList,CreateRegistration,IndexView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# app_name='Registration_Azizi'

urlpatterns=[
    url(r'^$',CreateRegistration.as_view(),name='Create_Registration'),
    url(r'^Successful/',IndexView.as_view(),name='Index_View'),
    # url(r'^RegistrationList/',views.RegistrationList.as_view(),name='Registration_List')
    url(r'^registrationlist/',login_required(RegistrationList.as_view()))
]
