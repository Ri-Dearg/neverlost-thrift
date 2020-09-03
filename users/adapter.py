from django.shortcuts import HttpResponseRedirect

from allauth.account.adapter import DefaultAccountAdapter


class CustomAdapter(DefaultAccountAdapter):
    """An adapter subclassed from django-allauth
    to utilise the "next" query request for redirection."""
    def respond_email_verification_sent(self, request, user):
        next = request.GET.get('next', '')
        return HttpResponseRedirect(next)
