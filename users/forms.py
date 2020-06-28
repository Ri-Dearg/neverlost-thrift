from django import forms
from django.utils.translation import gettext as _

from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class StyledSignupForm(SignupForm):
    """Custom styled signup form using crispy forms for alluth Signup"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email2"] = forms.EmailField(
            label=_("E-mail (again)"),
            widget=forms.TextInput(
                attrs={
                    'type': 'email',
                    'placeholder': _('Confirm Email')
                }
            )
        )

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username')
            ),
            Row(
                Column('email', css_class='col-md-6'),
                Column('email2', css_class='col-md-6')
            ),
            Row(
                Column('password1', css_class='col-md-6'),
                Column('password2', css_class='col-md-6')
            ),
            Submit('save', 'Join')
        )
