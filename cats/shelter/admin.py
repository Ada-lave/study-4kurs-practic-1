from django.contrib import admin
from shelter.models import Shelter, Cat, Adoption
# Register your models here.

@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    search_fields = ['name']
    sortable_by = ['name', 'capacity']

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'shelter']
    search_fields = ['name']
    list_filter = ['shelter__name']
    sortable_by = ['name', 'age']

@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    search_fields = ['adopter_name']