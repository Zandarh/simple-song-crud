from django.shortcuts import render
from django.http import JsonResponse
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def artiste_list(request, format=None):
    """Get all Artiste"""
    if request.method == 'GET':
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def artiste_detail(request, id, format=None):
    """Get all Artiste"""

    try:
       artistes = Artiste.objects.all(pk=id)
    except Artiste.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        """To get"""        
        serializer = ArtisteSerializer(artistes)
        return Response({"Artiste": serializer.data})
    
    elif request.method == 'PUT':
        serializer = ArtisteSerializer(artistes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artistes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def song_list(request, format=None):
    """Get all songs"""
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, id, format=None):
    """Get song details"""
    try:
        songs = Song.objects.all(pk=id)
    except Song.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        """To get"""
        serializer = SongSerializer(songs)
        return Response({"Songs": serializer.data})

    elif request.method == 'PUT':
        serializer = SongSerializer(songs, data=request.data)           
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def get_lyric(request, format=None):
    if request.method == 'GET':
        lyrics = Lyric.objects.all()
        lyric_serializer = LyricSerializer(lyrics, many=True)
        return Response(lyric_serializer.data)
    
    if request.method == 'POST':
        lyric_serializer = LyricSerializer(data=request.data)
        if lyric_serializer.is_valid:
            lyric_serializer.save()
            return Response(lyric_serializer.data, status=status.HTTP_201_CREATED)

'''ADVANCED LYRIC API'''
@api_view(['GET', 'PUT', 'DELETE'])
def  lyrics_detail(request, id, format=None):
    try:
        lyric = Lyric.objects.id(pk=id)
    except  Lyric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        lyric_serializer = LyricSerializer(lyric)
        return Response(lyric_serializer.data)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        lyric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
