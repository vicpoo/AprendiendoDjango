from django.shortcuts import render
from django.http import JsonResponse
from .models import Palabra
import random

def inicio(request):
    return render(request, 'juego/inicio.html')

def obtener_palabra(request, nivel):
    palabras = list(Palabra.objects.filter(nivel=nivel))
    if not palabras:
        return JsonResponse({'error': 'No hay palabras para este nivel'}, status=404)
    
    palabra = random.choice(palabras)
    otras_palabras = list(Palabra.objects.exclude(id=palabra.id))
    
    opciones = [p.palabra for p in random.sample(otras_palabras, min(3, len(otras_palabras)))] + [palabra.palabra]
    random.shuffle(opciones)
    
    # Extraer solo el nombre del archivo
    imagen_nombre = palabra.imagen.name.split('/')[-1] if palabra.imagen else ''
    audio_nombre = palabra.audio.name.split('/')[-1] if palabra.audio else ''
    
    return JsonResponse({
        'palabra': palabra.palabra,
        'imagen': imagen_nombre,
        'audio': audio_nombre,
        'opciones': opciones
    })