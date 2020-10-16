from django.urls import path, include
from .views import get_textlist, get_photolist

urlpatterns = [
    path('text', get_textlist, name='text'),
    path('photo', get_photolist, name='photo'),
]
