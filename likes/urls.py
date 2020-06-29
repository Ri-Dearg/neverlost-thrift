from django.urls import path

from .views import likes_toggle, LikesListView

urlpatterns = [
    path('', LikesListView.as_view(), name='likes-list'),
    path('ajax/toggle/', likes_toggle, name='likes-toggle'),
]
