from django.shortcuts import render
from .models import MediaContent

# Create your views here.

def media_content(request):
    media_content = MediaContent.objects.all()
    return render(request, 'main.html', {'media_content': media_content})