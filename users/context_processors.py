from allauth.account.forms import LoginForm

from .forms import StyledSignupForm


def login_form(request):
    return {'allauth_login_form': LoginForm()}


def signup_form(request):
    return {'allauth_signup_form': StyledSignupForm()}
