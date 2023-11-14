from django.contrib import admin
from .models import Artist, Genre, Style, Period, Artwork, Collection

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'born_date')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

class StyleAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('author', 'path', 'title', 'date', 'style', 'period', 'genre', 'image_url')
    list_filter = ('style', 'period', 'genre')
    
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'description')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Collection, CollectionAdmin)
