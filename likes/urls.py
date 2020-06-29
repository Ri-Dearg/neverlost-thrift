from django.urls import path

from .views import likes_toggle, update_likes, LikesListView

urlpatterns = [
    path('', LikesListView.as_view(), name='likes-list'),
    path('ajax/toggle/', likes_toggle, name='likes-toggle'),
    path('update/', update_likes, name='likes-update'),
]
