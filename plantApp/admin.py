from django.contrib import admin
from .models import Plant
# Register your models here.

class PlantAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name', 'disease_identified', 'created_at']

admin.site.register(Plant, PlantAdmin)