from django.urls import path, include
from .views import get_textlist, get_photolist, home

urlpatterns = [
    path('', home, name='home'),
    path('text', get_textlist, name='text'),
    path('photo', get_photolist, name='photo'),
]
