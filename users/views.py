from django.views.generic import TemplateView


class RenderJoinView(TemplateView):
    template_name = 'users/join.html'
