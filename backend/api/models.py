from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

class Character(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

class Appearance(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    is_main_character = models.BooleanField(default=False)