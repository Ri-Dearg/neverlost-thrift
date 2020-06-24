from django.urls import path

from .views import UserProfileDetailView

urlpatterns = [
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-detail')
]
