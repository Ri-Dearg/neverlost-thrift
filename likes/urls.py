from django.urls import path

from .views import add_to_likes, remove_from_likes, LikesListView

urlpatterns = [
    path('', LikesListView.as_view(), name='likes-list'),
    path('add/<int:item_id>/', add_to_likes, name='add-to-likes'),
    path('remove/<int:item_id>/', remove_from_likes, name='remove-from-likes')
]
