from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_content, name='media_content'),
]