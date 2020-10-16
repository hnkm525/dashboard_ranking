from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel

def get_textlist(request):
    return render(request, 'text.html')

def get_photolist(request):
    return render(request, 'photo.html')