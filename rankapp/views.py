from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel

def get_textlist(request):
    text_list = PostModel.objects.all()
    return render(request, 'text.html', {'object_list':text_list})

def get_photolist(request):
    photo_list = PostModel.objects.all()
    return render(request, 'photo.html', {'object_list':photo_list})

def home(request):
    return render(request, 'home.html')