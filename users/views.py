from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User

from allauth.account.views import EmailView, AddEmailForm
from allauth.account.utils import sync_user_email_addresses


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """Renders the user profile only if logged in"""
    model = User
    context_object_name = 'user'
    template_name = 'users/user_detail.html'

    def get_context_data(self, *args, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        # Selects the request user as user id no matter id is put in the url
        user = User.objects.get(pk=self.request.user.id)
        profile = user.userprofile

        # Makes field names user friendly
        field_names, values = profile._readable_field()

        add_email_form = AddEmailForm

        context['field_names'] = field_names
        context['values'] = values
        context['user'] = user
        context['profile'] = profile
        context['add_email_form'] = add_email_form
        return context


class CustomEmailView(EmailView):
    """Custom email editing view to maintain use on the profile page"""

    template_name = 'users/user_detail.html'

    def dispatch(self, request, *args, **kwargs):
        sync_user_email_addresses(request.user)
        user_id = User.objects.get(pk=self.request.user.id).id

        self.success_url = reverse_lazy('users:user-detail',
                                        kwargs={'pk': user_id})
        return super(EmailView, self).dispatch(request, *args, **kwargs)
