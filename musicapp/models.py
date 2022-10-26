from django.db import models

"""
Simple song crude app. With various models

Models = Artiste, Song and Lyric

Attributes for “Artiste” : first_name, last_name, age
Attributes for “Song” : title, date released, likes, artiste_id
Attributes for “Lyric”: content, song_id
"""

class Artiste(models.Model):
    """The Artite Model"""
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name 

class Song(models.Model):
    """The song model"""
    title = models.CharField(max_length=100, null=True, blank=True)
    date_released = models.DateField()
    likes = models.IntegerField(default=0, null=True, blank=True)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    """Lyric model"""
    content = models.TextField(null=True, blank=True)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content
