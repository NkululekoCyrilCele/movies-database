from django.contrib import admin
from .models import MovieGenre, MovieList


class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieListAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'in_stock', 'daily_rate')


admin.site.register(MovieGenre, MovieGenreAdmin)
admin.site.register(MovieList, MovieListAdmin)
