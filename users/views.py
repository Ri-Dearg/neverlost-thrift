from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/user_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        profile = user.userprofile
        field_names, values = profile._readable_field()

        context['field_names'] = field_names
        context['values'] = values
        context['user'] = user
        context['profile'] = profile
        return context
