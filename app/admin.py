from django.contrib import admin

#Для альбома
from app.models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug', 'img']})
    ]
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}
    ordering = ['title']
#
#Для фотографии
class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['title', 'album', 'img']})
    ]
    list_display = ['title', 'album']
    ordering = ['title']
#
#Регистрируем
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
