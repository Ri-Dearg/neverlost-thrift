from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Email


class CreateEmailView(SuccessMessageMixin, CreateView):
    model = Email
    context_object_name = 'email'
    fields = ['sender', 'name', 'subject', 'message']
    success_message = 'Thank you, your message has been sent'

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        # Details necessary for Stripe payment processing
        contact_active = True

        context['contact_active'] = contact_active
        return context
