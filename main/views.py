from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

from django.contrib import messages
from django.urls import reverse_lazy

from main import forms
from main import models

import logging

logger = logging.getLogger(__name__)


class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/contact_us_sent"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
