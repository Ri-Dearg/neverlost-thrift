from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib.auth.models import User


@login_required
def access_only_own_profile(request):
    user_id = request.user.id
    reverse('users:detail', user_id)


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/user_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(pk=self.request.user.id)
        return context
