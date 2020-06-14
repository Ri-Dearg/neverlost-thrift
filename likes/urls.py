from django.urls import path

from .views import add_to_likes, remove_from_likes, LikesListView

urlpatterns = [
    path('', LikesListView.as_view(), name='list'),
    path('add/<int:item_id>/', add_to_likes, name='add_to_likes'),
    path('remove/<int:item_id>/', remove_from_likes, name='remove_from_likes')
]
