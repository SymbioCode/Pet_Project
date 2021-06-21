from django.contrib import admin
from books.models import *

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Genre, GenreAdmin)

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('id', 'name', 'name_of_author', 'number_of_edition',
                    'year_of_edition','description','count_of_pages','book_cover','pages_of_book','user','genre',
                     'is_allowed_to_exchange', 'is_exchanged')
    list_display_links = ('name',)
    search_fields = ('name', 'name_of_author', 'genre', 'user')
    list_filter = ('name', 'user')


admin.site.register(Book, BookAdmin)
admin.site.register(Review)
