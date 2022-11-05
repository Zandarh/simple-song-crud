from rest_framework import serializers
from .models import Artiste, Song, Lyric

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['id', 'first_name', 'last_name', 'age']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Song
        fields = ['title', 'date released', 'likes', 'artiste_id']

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        field = ['content', 'song_id']