from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views
from main import views
from main import models
from main import forms

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("contact_us/", views.ContactUsView.as_view(), name="contact_us"),
    path("contact_us_sent/", TemplateView.as_view(template_name="contact_form_sent.html"), name="contact_us_sent"),
]

