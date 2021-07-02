from django.contrib import admin

from .models import Books, Comment


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'book', 'image', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'context')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


admin.site.register(Books, BooksAdmin)

admin.site.register(Comment, CommentAdmin)
