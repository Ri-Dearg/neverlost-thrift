from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import model_to_dict
from django.contrib.auth.decorators import login_required

from allauth.account.views import (EmailView,
                                   AddEmailForm,
                                   ChangePasswordForm,
                                   PasswordChangeView,
                                   sensitive_post_parameters_m)
from allauth.account.utils import sync_user_email_addresses

from .forms import UserProfileForm


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """Renders the user profile only if logged in."""
    model = User
    context_object_name = 'user'
    template_name = 'users/user_detail.html'

    def get_context_data(self, *args, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        # Selects the request user as user id no matter id is put in the url
        user = User.objects.get(pk=self.request.user.id)
        profile = user.userprofile
        userprofile_dict = model_to_dict(profile)

        # Adds the forms to the page,
        # setting shipping and billing to saved info.
        add_email_form = AddEmailForm()
        change_password_form = ChangePasswordForm
        user_profile_detail = UserProfileForm(initial=userprofile_dict)

        context['user_profile_detail'] = user_profile_detail
        context['user'] = user
        context['profile'] = profile
        context['add_email_form'] = add_email_form
        context['change_password_form'] = change_password_form
        return context


class CustomEmailView(LoginRequiredMixin, EmailView):
    """Custom email editing view subclassing django-allauth's EMailView
    to maintain use and redirection on the profile page.
    Essentially this is a another DetailView profile page but
    as it is incredibly difficult to have allauth utilise alternative views
    for some functions it was easier to utilise alternative views with
    the same template and context as the basic UserProfile Detailview.
    Apart from the url difference it should be unnoticable to the user."""

    template_name = 'users/user_detail.html'

    def dispatch(self, request, *args, **kwargs):

        # Retrieves user's emails
        sync_user_email_addresses(request.user)
        user_id = User.objects.get(pk=self.request.user.id).id

        # Returns the user to the profile page on success
        self.success_url = reverse_lazy('users:user-detail',
                                        kwargs={'pk': user_id})
        return super(CustomEmailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        """Adds all necessary information to the context."""
        context = super().get_context_data(**kwargs)
        # Selects the request user as user id no matter id is put in the url
        user = User.objects.get(pk=self.request.user.id)
        profile = user.userprofile
        userprofile_dict = model_to_dict(profile)

        # Adds the forms to the page,
        # setting shipping and billing to saved info.
        add_email_form = AddEmailForm()
        change_password_form = ChangePasswordForm
        user_profile_detail = UserProfileForm(initial=userprofile_dict)

        context['user_profile_detail'] = user_profile_detail
        context['user'] = user
        context['profile'] = profile
        context['add_email_form'] = add_email_form
        context['change_password_form'] = change_password_form
        return context


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """Custom password editing view subclassing django-allauth's PasswordChangeView
    to maintain use and redirection on the profile page.
    Essentially this is a another DetailView profile page but
    as it is incredibly difficult to have allauth utilise alternative views
    for some functions it was easier to utilise alternative views with
    the same template and context as the basic UserProfile Detailview.
    Apart from the url difference it should be unnoticable to the user."""

    template_name = 'users/user_detail.html'

    @sensitive_post_parameters_m
    def dispatch(self, request, *args, **kwargs):
        user_id = User.objects.get(pk=self.request.user.id).id

        self.success_url = reverse_lazy('users:user-detail',
                                        kwargs={'pk': user_id})

        return super(CustomPasswordChangeView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        # Selects the request user as user id no matter id is put in the url
        user = User.objects.get(pk=self.request.user.id)
        profile = user.userprofile
        userprofile_dict = model_to_dict(profile)

        # Adds the forms to the page,
        # setting shipping and billing to saved info.
        add_email_form = AddEmailForm()
        change_password_form = ChangePasswordForm
        user_profile_detail = UserProfileForm(initial=userprofile_dict)

        context['user_profile_detail'] = user_profile_detail
        context['user'] = user
        context['profile'] = profile
        context['add_email_form'] = add_email_form
        context['change_password_form'] = change_password_form
        return context


@login_required
def update_shipping_billing(request):
    """Updates the user's Shipping and Billing information."""
    # Retrieves the current user and redirection page.
    user = request.user
    userprofile = user.userprofile
    next = request.GET.get('next', '')
    if request.method == 'POST':
        data = request.POST
        form = UserProfileForm(data=data)
        if form.is_valid():
            # Make sure the correct user is applied to the profile
            # before committing and updating info
            form = UserProfileForm(instance=userprofile, data=data)
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Your information has been updated')
            return HttpResponseRedirect(next)
        else:
            form = UserProfileForm()
            messages.warning(request, 'Failed to update your information. \
                Please Check your details.')
            return HttpResponseRedirect(next)
