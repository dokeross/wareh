from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^contact/$', views.contactform, name='contact'),
    url(r'^contact_phone/$', views.contactform_phone, name='contact_phone'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
