from django.shortcuts import render
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer


def artiste_list(request):
    """Get all """

# Create your views here.
