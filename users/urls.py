from django.urls import path
from .views import RenderJoinView

urlpatterns = [
    path('join/', RenderJoinView.as_view(), name="join"),
]
