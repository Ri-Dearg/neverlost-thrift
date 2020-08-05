from django.shortcuts import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone

from django.db import models

from config import settings


class Email(models.Model):
    email = models.EmailField(blank=False, null=False)
    name = models.CharField(max_length=60, blank=False, null=False)
    subject = models.CharField(max_length=254, blank=False, null=False)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('contact:email-form')

    def save(self, *args, **kwargs):
        email = self.email
        name = self.name
        subject = self.subject
        message = self.message

        contact_subject = render_to_string(
            'contact/emails/contact_subject.txt',
            {'subject': subject})
        contact_body = render_to_string(
            'contact/emails/contact_body.txt',
            {'name': name, 'email': email, 'message': message})
        send_mail(contact_subject,
                  contact_body,
                  email,
                  [settings.DEFAULT_FROM_EMAIL])

        thanks_subject = render_to_string(
            'contact/emails/thanks_subject.txt',
            {'subject': subject})
        thanks_body = render_to_string(
            'contact/emails/thanks_body.txt',
            {'name': name})
        send_mail(thanks_subject,
                  thanks_body,
                  settings.DEFAULT_FROM_EMAIL,
                  [email])

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email}, {self.subject}'
