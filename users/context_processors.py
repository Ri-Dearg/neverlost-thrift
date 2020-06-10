from allauth.account.forms import LoginForm


def login_form(request):
    return {'allauth_login_form': LoginForm()}
