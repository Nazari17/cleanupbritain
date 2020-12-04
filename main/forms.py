from django import forms
from django.forms import inlineformset_factory
from django.core.mail import send_mail
from django.contrib.auth.forms import (UserCreationForm as DjangoUserCreationForm)
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import authenticate
from django.conf import settings
#from . import models
#from . import widgets
import logging

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length = 28)
    lastname = forms.CharField(label='Family Name', max_length = 56)
    phone = forms.CharField(label='Phone', required=False, max_length = 24)
    email = forms.EmailField(label='eMail')
    subject = forms.CharField(label='Subject', max_length=48)
    message = forms.CharField(max_length = 600, widget=forms.Textarea)

    def send_mail(self):
        """import pdb; pdb.set_trace()"""
        logger.info("Sending email to customer service")
        mail_content = "{0} {1}\n\nphone: {2} \nmail: {3}\n\nsends you this message:\n\nsubject: {4} \n\n{5}".format(
            self.cleaned_data["firstname"],
            self.cleaned_data["lastname"],
            self.cleaned_data["phone"],
            self.cleaned_data["email"],
            self.cleaned_data["subject"],
            self.cleaned_data["message"],
        )
        send_mail(
            "Contact Request from cleanupbritain website",
            mail_content,
            '',
            ['nazaridm17@gmail.com'],
            fail_silently=False,
        )
