from django.contrib import admin
from .models import Palabra

@admin.register(Palabra)
class PalabraAdmin(admin.ModelAdmin):
    list_display = ('palabra', 'nivel')
    list_filter = ('nivel',)
    search_fields = ('palabra',)