from allauth.account.forms import LoginForm

from .forms import StyledSignupForm


def login_form(request):
    """Creates context for a login form custom template"""
    return {'allauth_login_form': LoginForm()}


def signup_form(request):
    """Creates context for a signup form custom template"""
    return {'allauth_signup_form': StyledSignupForm()}
