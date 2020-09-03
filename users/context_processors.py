from allauth.account.forms import LoginForm

from .forms import StyledSignupForm


def login_form(request):
    """Creates context for a login form custom template
    and sends it for validation."""
    if 'login' and 'password' in request.POST:
        return {'allauth_login_form': LoginForm(request.POST)}
    else:
        return {'allauth_login_form': LoginForm()}


def signup_form(request):
    """Creates context for a signup form custom template
    and sends it for validation."""
    if 'username' and 'email' and 'email2' in request.POST:
        return {'allauth_signup_form': StyledSignupForm(request.POST)}
    else:
        return {'allauth_signup_form': StyledSignupForm()}
