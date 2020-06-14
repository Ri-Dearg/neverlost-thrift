from django.urls import path

from .views import add_to_likes

urlpatterns = [
    path('add/<int:item_id>/', add_to_likes, name='add_to_likes')
]
