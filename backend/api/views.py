# backend/api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Anime, Character, Appearance
import json

@csrf_exempt
def anime_view(request):
    if request.method == 'GET':
        animes = list(Anime.objects.values())
        return JsonResponse(animes, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        # Check if anime with same title exists
        if Anime.objects.filter(title=data['title']).exists():
            return JsonResponse({'error': 'An anime with this title already exists'}, status=400)
        anime = Anime.objects.create(title=data['title'], description=data['description'], release_date=data['release_date'])
        return JsonResponse({'id': anime.id, 'title': anime.title, 'description': anime.description, 'release_date': anime.release_date})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        anime = Anime.objects.get(id=data['id'])
        anime.title = data['title']
        anime.description = data['description']
        anime.release_date = data['release_date']
        anime.save()
        return JsonResponse({'id': anime.id, 'title': anime.title, 'description': anime.description, 'release_date': anime.release_date})
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        anime = Anime.objects.get(id=data['id'])
        # Delete related appearances first
        Appearance.objects.filter(anime=anime).delete()
        anime.delete()
        return JsonResponse({'status': 'deleted'})

@csrf_exempt
def character_view(request):
    if request.method == 'GET':
        characters = list(Character.objects.values())
        return JsonResponse(characters, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        # Check if character with same name exists
        if Character.objects.filter(name=data['name']).exists():
            return JsonResponse({'error': 'A character with this name already exists'}, status=400)
        character = Character.objects.create(name=data['name'], bio=data['bio'])
        return JsonResponse({'id': character.id, 'name': character.name, 'bio': character.bio})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        character = Character.objects.get(id=data['id'])
        character.name = data['name']
        character.bio = data['bio']
        character.save()
        return JsonResponse({'id': character.id, 'name': character.name, 'bio': character.bio})
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        character = Character.objects.get(id=data['id'])
        # Delete related appearances first
        Appearance.objects.filter(character=character).delete()
        character.delete()
        return JsonResponse({'status': 'deleted'})

@csrf_exempt
def appearance_view(request):
    if request.method == 'GET':
        appearances = list(Appearance.objects.select_related('anime', 'character').values(
            'id', 
            'anime_id', 
            'anime__title',
            'character_id', 
            'character__name',
            'role', 
            'is_main_character'
        ))
        return JsonResponse(appearances, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        # Check if appearance with same anime and character exists
        if Appearance.objects.filter(anime_id=data['anime_id'], character_id=data['character_id']).exists():
            return JsonResponse({'error': 'This character already appears in this anime'}, status=400)
        appearance = Appearance.objects.create(
            anime_id=data['anime_id'],
            character_id=data['character_id'],
            role=data['role'],
            is_main_character=data['is_main_character']
        )
        appearance_data = Appearance.objects.select_related('anime', 'character').values(
            'id', 'anime_id', 'anime__title', 'character_id', 'character__name',
            'role', 'is_main_character'
        ).get(id=appearance.id)
        return JsonResponse(appearance_data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        appearance = Appearance.objects.get(id=data['id'])
        appearance.anime_id = data['anime_id']
        appearance.character_id = data['character_id']
        appearance.role = data['role']
        appearance.is_main_character = data['is_main_character']
        appearance.save()
        appearance_data = Appearance.objects.select_related('anime', 'character').values(
            'id', 'anime_id', 'anime__title', 'character_id', 'character__name',
            'role', 'is_main_character'
        ).get(id=appearance.id)
        return JsonResponse(appearance_data)
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        Appearance.objects.get(id=data['id']).delete()
        return JsonResponse({'status': 'deleted'})